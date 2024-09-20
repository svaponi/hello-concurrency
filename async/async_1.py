import asyncio
import random


async def display_date(num, loop_):
    end_time = loop_.time() + 10.0
    while loop_.time() < end_time:
        print(f"Loop: {num} :: {round(end_time - loop_.time(), 3)}")
        await asyncio.sleep(random.random() * 5)
    print(f"Loop: {num} :: done")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    fut1 = asyncio.ensure_future(display_date(1, loop))
    fut2 = asyncio.ensure_future(display_date(2, loop))
    fut3 = asyncio.ensure_future(display_date(3, loop))

    loop.run_until_complete(fut1)
    loop.run_until_complete(fut2)
    loop.run_until_complete(fut3)

    print(f"Done")
