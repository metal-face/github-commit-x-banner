import asyncio
import os
import httpx
from tweepy import OAuth1UserHandler, API
from cairosvg import svg2png


async def update_x_banner():
    github_user = os.getenv("X_GITHUB_USERNAME")
    chart_url = f"https://ghchart.rshah.org/151515/{github_user}"

    async with httpx.AsyncClient() as client:
        response = await client.get(chart_url)

    if response.status_code != 200:
        print("Failed to fetch GitHub graph.")
        return

    with open("github_graph.svg", "wb") as f:
        f.write(response.content)

    # svg2png is synchronous, run in a thread to avoid blocking the event loop
    await asyncio.to_thread(
        svg2png,
        url='github_graph.svg',
        write_to='banner.png',
        output_width=1500,
        output_height=500
    )

    auth = OAuth1UserHandler(
        os.getenv("X_API_KEY"),
        os.getenv("X_API_SECRET"),
        os.getenv("X_ACCESS_TOKEN"),
        os.getenv("X_ACCESS_SECRET")
    )
    api = API(auth)

    # tweepy's v1.1 API is synchronous, run in a thread to avoid blocking the event loop
    await asyncio.to_thread(api.update_profile_banner, "banner.png")
    print("X banner updated successfully!")


if __name__ == "__main__":
    asyncio.run(update_x_banner())
