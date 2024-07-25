"""
HW 27
"""
import aiohttp
import asyncio
import time

async def fetch(session, url):
    """_summary_

    Args:
        session (_type_): _description_
        url (_type_): _description_

    Returns:
        _type_: _description_
    """
    async with session.get(url) as response:
        return await response.text()
async def fetch_all(urls):
    """_summary_

    Args:
        urls (_type_): _description_

    Returns:
        _type_: _description_
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
def main():
    """_summary_
    """
    urls = ["http://example.com"] * 100
    start_time = time.time()
    asyncio.run(fetch_all(urls))
    end_time = time.time()
    print(f"Время затрачено: {end_time - start_time} секунд")


if __name__ == "__main__":
    main()
