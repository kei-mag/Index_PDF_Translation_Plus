import asyncio

async def async_task():
    await asyncio.sleep(5)
    return "Task completed!"

async def main():
    task = asyncio.create_task(async_task())
    
    while not task.done():
        print("Not yet")
        await asyncio.sleep(1)
    
    result = await task
    print(result)

if __name__ == "__main__":
    asyncio.run(main())