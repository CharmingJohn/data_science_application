import asyncio


async def printer(name: str, times: int) -> None:
    for i in range(times):
        print(name)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        printer('A', 3),
        printer('B', 5),
    )

asyncio.run(main())