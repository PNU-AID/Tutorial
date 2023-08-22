import asyncio
import time


async def wait_network():
    print("네트워크 다운로드 중...")
    await asyncio.sleep(3.0)

async def func1():

    start = time.time()

    task1 = asyncio.create_task(wait_network())
    task2 = asyncio.create_task(wait_network())

    await task1
    await task2

    end = time.time()

    delta = end-start
    print(f"총 시간: {delta:.3f} sec")



if __name__ == "__main__":
    asyncio.run(func1())