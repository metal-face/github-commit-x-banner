import os
from requests import get
from tweepy import OAuth1UserHandler, API
from cairosvg import svg2png


def update_x_banner():
    github_user = os.getenv("GITHUB_USERNAME")
    # Fetch the graph. The '151515' adds a dark theme background.
    chart_url = f"https://ghchart.rshah.org/151515/{github_user}"

    response = get(chart_url)
    if response.status_code != 200:
        print("Failed to fetch GitHub graph.")
        return

    with open("github_graph.svg", "wb") as f:
        f.write(response.content)

    # Convert SVG to PNG and scale it to X's 1500x500 banner dimensions
    svg2png(
        url='github_graph.svg',
        write_to='banner.png',
        output_width=1500,
        output_height=500
    )

    # Authenticate with the X API (OAuth 1.0a is required for profile updates)
    auth = OAuth1UserHandler(
        os.getenv("X_API_KEY"),
        os.getenv("X_API_SECRET"),
        os.getenv("X_ACCESS_TOKEN"),
        os.getenv("X_ACCESS_SECRET")
    )
    api = API(auth)

    # Upload the new banner
    api.update_profile_banner("banner.png")
    print("X banner updated successfully!")


if __name__ == "__main__":
    update_x_banner()