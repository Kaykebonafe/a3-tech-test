import aiohttp
import asyncio

async def make_request():
    json_data = {
        "query": "Como parar de fumar?"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("http://localhost:5000/chat/query", json=json_data, headers={"Content-Type": "application/json"}) as response:
                return await response.json()
    except asyncio.TimeoutError:
        print("Request timed out")
        return None

async def main():
    response = await make_request()
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
