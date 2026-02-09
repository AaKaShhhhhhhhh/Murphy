import logging
from mcp import MCPServer
from .client import SlackClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("slack_server")

class SlackServer(MCPServer):
    def __init__(self):
        super().__init__("slack-server")
        self.client = SlackClient()

    async def post_message(self, channel: str, text: str, thread_ts: str = None):
        logger.info(f"Posting message to channel {channel}")
        return await self.client.post_message(channel, text, thread_ts)

    async def get_channel_history(self, channel: str, limit: int = 10, oldest: str = None):
        logger.info(f"Fetching channel history for {channel}")
        return await self.client.get_channel_history(channel, limit, oldest)

    async def search_messages(self, query: str, count: int = 20):
        logger.info(f"Searching messages with query: {query}")
        return await self.client.search_messages(query, count)

    async def update_message(self, channel: str, timestamp: str, text: str):
        logger.info(f"Updating message in channel {channel} at {timestamp}")
        return await self.client.update_message(channel, timestamp, text)

    async def add_reaction(self, channel: str, timestamp: str, emoji: str):
        logger.info(f"Adding reaction {emoji} to message in channel {channel} at {timestamp}")
        return await self.client.add_reaction(channel, timestamp, emoji)

if __name__ == "__main__":
    server = SlackServer()
    server.run()