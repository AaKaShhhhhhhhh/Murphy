import logging
from mcp import MCPServer
from .client import GitHubClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("github_server")

class GitHubServer(MCPServer):
    def __init__(self):
        super().__init__("github-server")
        self.client = GitHubClient()

    async def get_recent_deployments(self, repo: str, limit: int = 10):
        logger.info(f"Fetching recent deployments for repo: {repo}")
        return await self.client.get_recent_deployments(repo, limit)

    async def get_deployment_status(self, repo: str, deployment_id: int):
        logger.info(f"Fetching deployment status for repo: {repo}, deployment_id: {deployment_id}")
        return await self.client.get_deployment_status(repo, deployment_id)

    async def search_issues(self, repo: str, query: str, labels: list = None, state: str = "all"):
        logger.info(f"Searching issues in repo: {repo} with query: {query}")
        return await self.client.search_issues(repo, query, labels, state)

    async def get_commit_details(self, repo: str, sha: str):
        logger.info(f"Fetching commit details for repo: {repo}, sha: {sha}")
        return await self.client.get_commit_details(repo, sha)

    async def create_issue(self, repo: str, title: str, body: str, labels: list = None, assignees: list = None):
        logger.info(f"Creating issue in repo: {repo} with title: {title}")
        return await self.client.create_issue(repo, title, body, labels, assignees)

    async def get_pr_details(self, repo: str, pr_number: int):
        logger.info(f"Fetching PR details for repo: {repo}, PR number: {pr_number}")
        return await self.client.get_pr_details(repo, pr_number)

    async def search_code(self, repo: str, query: str, path: str = None):
        logger.info(f"Searching code in repo: {repo} with query: {query}")
        return await self.client.search_code(repo, query, path)

if __name__ == "__main__":
    server = GitHubServer()
    server.run()