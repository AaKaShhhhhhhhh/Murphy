import os
import logging
from typing import Optional, List
import httpx
from .models import Deployment, DeploymentStatus, Issue, CommitDetails, PullRequest, CodeSearchResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("github_client")

class GitHubClient:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.token = os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GITHUB_TOKEN environment variable is not set.")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    async def get_recent_deployments(self, repo: str, limit: int = 10) -> List[Deployment]:
        url = f"{self.base_url}/repos/{repo}/deployments"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params={"per_page": limit})
            logger.info(f"GET {url} - {response.status_code}")
            response.raise_for_status()
            return [Deployment(**item) for item in response.json()]

    async def get_deployment_status(self, repo: str, deployment_id: int) -> DeploymentStatus:
        url = f"{self.base_url}/repos/{repo}/deployments/{deployment_id}/statuses"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            logger.info(f"GET {url} - {response.status_code}")
            response.raise_for_status()
            statuses = response.json()
            if statuses:
                return DeploymentStatus(**statuses[0])
            raise ValueError("No statuses found for deployment.")

    async def search_issues(self, repo: str, query: str, labels: Optional[List[str]] = None, state: str = "all") -> List[Issue]:
        url = f"{self.base_url}/repos/{repo}/issues"
        params = {"q": query, "state": state}
        if labels:
            params["labels"] = ",".join(labels)
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params=params)
            logger.info(f"GET {url} - {response.status_code}")
            response.raise_for_status()
            return [Issue(**item) for item in response.json()]

    async def get_commit_details(self, repo: str, sha: str) -> CommitDetails:
        url = f"{self.base_url}/repos/{repo}/commits/{sha}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            logger.info(f"GET {url} - {response.status_code}")
            response.raise_for_status()
            data = response.json()
            return CommitDetails(
                sha=data["sha"],
                message=data["commit"]["message"],
                author=data["commit"]["author"]["name"],
                date=data["commit"]["author"]["date"],
                files_changed=[file["filename"] for file in data.get("files", [])],
                stats=data.get("stats", {})
            )

    async def create_issue(self, repo: str, title: str, body: str, labels: Optional[List[str]] = None, assignees: Optional[List[str]] = None) -> Issue:
        url = f"{self.base_url}/repos/{repo}/issues"
        payload = {"title": title, "body": body}
        if labels:
            payload["labels"] = labels
        if assignees:
            payload["assignees"] = assignees
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, json=payload)
            logger.info(f"POST {url} - {response.status_code}")
            response.raise_for_status()
            return Issue(**response.json())

    async def get_pr_details(self, repo: str, pr_number: int) -> PullRequest:
        url = f"{self.base_url}/repos/{repo}/pulls/{pr_number}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            logger.info(f"GET {url} - {response.status_code}")
            response.raise_for_status()
            data = response.json()
            return PullRequest(
                title=data["title"],
                body=data.get("body"),
                state=data["state"],
                merged_at=data.get("merged_at"),
                mergeable=data.get("mergeable"),
                changed_files=data["changed_files"]
            )

    async def search_code(self, repo: str, query: str, path: Optional[str] = None) -> List[CodeSearchResult]:
        url = f"{self.base_url}/search/code"
        params = {"q": f"{query} repo:{repo}"}
        if path:
            params["q"] += f" path:{path}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params=params)
            logger.info(f"GET {url} - {response.status_code}")
            response.raise_for_status()
            return [
                CodeSearchResult(
                    file_path=item["path"],
                    matches=[match["fragment"] for match in item.get("text_matches", [])],
                    url=item["html_url"]
                )
                for item in response.json().get("items", [])
            ]