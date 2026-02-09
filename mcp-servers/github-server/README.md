# GitHub MCP Server

This is the GitHub MCP Server implementation for interacting with GitHub's REST API v3.

## Features

- Fetch recent deployments
- Get deployment status
- Search issues and pull requests
- Get commit details
- Create new issues
- Get pull request details
- Search code in repositories

## Setup

1. **Install dependencies**:

   ```bash
   uv pip install -e .
   ```

2. **Set environment variables**:

   Copy `.env.example` to `.env` and fill in your GitHub token:

   ```bash
   cp .env.example .env
   ```

3. **Run the server**:

   ```bash
   uv run python src/github_server/server.py
   ```

## Environment Variables

- `GITHUB_TOKEN`: Your GitHub Personal Access Token for authentication.

## Example Usage

### Get Recent Deployments

```python
response = await server.get_recent_deployments(repo="owner/repo", limit=5)
print(response)
```

### Get Deployment Status

```python
response = await server.get_deployment_status(repo="owner/repo", deployment_id=12345)
print(response)
```

### Search Issues

```python
response = await server.search_issues(repo="owner/repo", query="bug", labels=["critical"], state="open")
print(response)
```

### Get Commit Details

```python
response = await server.get_commit_details(repo="owner/repo", sha="abc123")
print(response)
```

### Create Issue

```python
response = await server.create_issue(repo="owner/repo", title="New Issue", body="Issue details here.", labels=["bug"], assignees=["user1"])
print(response)
```

### Get Pull Request Details

```python
response = await server.get_pr_details(repo="owner/repo", pr_number=42)
print(response)
```

### Search Code

```python
response = await server.search_code(repo="owner/repo", query="def function_name", path="src/")
print(response)
```