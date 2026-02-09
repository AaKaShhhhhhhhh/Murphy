import os
import logging
from typing import Optional, List
import httpx
from .types import SlackMessage, PostMessageResponse, ChannelHistoryResponse, SearchMessagesResponse, UpdateMessageResponse, AddReactionResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("slack_client")

class SlackClient:
    def __init__(self):
        self.base_url = "https://slack.com/api/"
        self.token = os.getenv("SLACK_BOT_TOKEN")
        if not self.token:
            raise ValueError("SLACK_BOT_TOKEN environment variable is not set.")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    async def post_message(self, channel: str, text: str, thread_ts: Optional[str] = None) -> PostMessageResponse:
        url = f"{self.base_url}chat.postMessage"
        payload = {"channel": channel, "text": text}
        if thread_ts:
            payload["thread_ts"] = thread_ts
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, json=payload)
            logger.info(f"POST {url} - {response.status_code}")
            return PostMessageResponse(**response.json())

    async def get_channel_history(self, channel: str, limit: int = 10, oldest: Optional[str] = None) -> ChannelHistoryResponse:
        url = f"{self.base_url}conversations.history"
        params = {"channel": channel, "limit": limit}
        if oldest:
            params["oldest"] = oldest
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params=params)
            logger.info(f"GET {url} - {response.status_code}")
            return ChannelHistoryResponse(**response.json())

    async def search_messages(self, query: str, count: int = 20) -> SearchMessagesResponse:
        url = f"{self.base_url}search.messages"
        params = {"query": query, "count": count}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params=params)
            logger.info(f"GET {url} - {response.status_code}")
            return SearchMessagesResponse(**response.json())

    async def update_message(self, channel: str, timestamp: str, text: str) -> UpdateMessageResponse:
        url = f"{self.base_url}chat.update"
        payload = {"channel": channel, "ts": timestamp, "text": text}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, json=payload)
            logger.info(f"POST {url} - {response.status_code}")
            return UpdateMessageResponse(**response.json())

    async def add_reaction(self, channel: str, timestamp: str, emoji: str) -> AddReactionResponse:
        url = f"{self.base_url}reactions.add"
        payload = {"channel": channel, "timestamp": timestamp, "name": emoji}
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, json=payload)
            logger.info(f"POST {url} - {response.status_code}")
            return AddReactionResponse(**response.json())