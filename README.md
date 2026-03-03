# github-commit-x-banner

Automatically updates your X (Twitter) profile banner with your GitHub contribution graph.

## How It Works

1. Fetches your GitHub contribution graph as an SVG from [ghchart.rshah.org](https://ghchart.rshah.org)
2. Converts the SVG to a PNG scaled to X's banner dimensions (1500x500)
3. Uploads the PNG as your X profile banner via the X API

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) for dependency management
- A GitHub account
- An X developer account with OAuth 1.0a credentials

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/github-commit-x-banner.git
   cd github-commit-x-banner
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Set the required environment variables:

   ```bash
   export GITHUB_USERNAME=your_github_username
   export X_API_KEY=your_x_api_key
   export X_API_SECRET=your_x_api_secret
   export X_ACCESS_TOKEN=your_x_access_token
   export X_ACCESS_SECRET=your_x_access_secret
   ```

## Usage

```bash
uv run main.py
```

## X API Credentials

You need an X developer account with an app that has **Read and Write** permissions. OAuth 1.0a credentials (API key, API secret, access token, access secret) are required as X's v1.1 API is used for profile banner updates.

Create an app at [developer.x.com](https://developer.x.com).

## Dependencies

- [cairosvg](https://cairosvg.org/) — SVG to PNG conversion
- [requests](https://docs.python-requests.org/) — HTTP requests to fetch the GitHub graph
- [tweepy](https://www.tweepy.org/) — X API client
