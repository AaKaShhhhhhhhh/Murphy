# Slack MCP Server

This is the Slack MCP Server implementation for interacting with Slack's Web API.

## Features

- Post messages to Slack channels
- Retrieve channel history
- Search messages across the workspace
- Update existing messages
- Add reactions to messages

## Setup

1. **Install dependencies**:

   ```bash
   uv pip install -e .
   ```

2. **Set environment variables**:

   Copy `.env.example` to `.env` and fill in your Slack bot token:

   ```bash
   cp .env.example .env
   ```

3. **Run the server**:

   ```bash
   uv run python src/slack_server/server.py
   ```

## Environment Variables

- `SLACK_BOT_TOKEN`: Your Slack bot token for authentication.

## Example Usage

### Post a Message

```python
response = await server.post_message(channel="#general", text="Hello, world!")
print(response)
```

### Get Channel History

```python
response = await server.get_channel_history(channel="#general", limit=5)
print(response)
```

### Search Messages

```python
response = await server.search_messages(query="incident")
print(response)
```

### Update a Message

```python
response = await server.update_message(channel="#general", timestamp="1234567890.123456", text="Updated text")
print(response)
```

### Add a Reaction

```python
response = await server.add_reaction(channel="#general", timestamp="1234567890.123456", emoji="thumbsup")
print(response)
```