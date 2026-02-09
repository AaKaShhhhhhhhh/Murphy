from typing import Optional, List
from pydantic import BaseModel

class Deployment(BaseModel):
    deployment_id: int
    sha: str
    environment: str
    created_at: str
    creator: str

class DeploymentStatus(BaseModel):
    state: str
    description: Optional[str]
    created_at: str

class Issue(BaseModel):
    issue_number: int
    title: str
    body: Optional[str]
    state: str
    labels: List[str]
    created_at: str

class CommitDetails(BaseModel):
    sha: str
    message: str
    author: str
    date: str
    files_changed: List[str]
    stats: dict

class PullRequest(BaseModel):
    title: str
    body: Optional[str]
    state: str
    merged_at: Optional[str]
    mergeable: Optional[bool]
    changed_files: int

class CodeSearchResult(BaseModel):
    file_path: str
    matches: List[str]
    url: str