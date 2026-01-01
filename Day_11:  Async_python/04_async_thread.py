from concurrent.futures import ThreadPoolExecutor
import time
import asyncio

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3)
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Lemon Tea")
        print(result)

asyncio.run(main())