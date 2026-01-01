import asyncio

async def brew_tea():
    print("Tea is brewing...!!")
    await asyncio.sleep(2)
    print("Tea is ready.")

asyncio.run(brew_tea())