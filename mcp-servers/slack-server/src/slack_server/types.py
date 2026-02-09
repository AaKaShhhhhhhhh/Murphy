from typing import Optional, List
from pydantic import BaseModel

class SlackMessage(BaseModel):
    user: str
    text: str
    timestamp: str

class PostMessageResponse(BaseModel):
    ok: bool
    ts: Optional[str]
    error: Optional[str]

class ChannelHistoryResponse(BaseModel):
    messages: List[SlackMessage]
    ok: bool
    error: Optional[str]

class SearchMessagesResponse(BaseModel):
    messages: List[SlackMessage]
    ok: bool
    error: Optional[str]

class UpdateMessageResponse(BaseModel):
    ok: bool
    error: Optional[str]

class AddReactionResponse(BaseModel):
    ok: bool
    error: Optional[str]
