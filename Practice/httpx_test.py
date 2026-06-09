import httpx
import asyncio

#httpx that supports both synchronous and asynchronous requests, making it a versatile choice for various applications. It also provides features like connection pooling, HTTP/2 support, and built-in support for cookies and authentication.
response = httpx.get("https://api.github.com")
print(response.status_code)


response = httpx.get(
    "https://jsonplaceholder.typicode.com/users/1"
)
# print(response.json())


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get( "https://weather-api.com/current")
        print(response)

asyncio.run(main())