import asyncio

async def brew_tea(name):
    print(f"Brewing {name} tea.")
    await asyncio.sleep(3)
    print(f"{name} tea is ready.")

async def main():
    await asyncio.gather(
    brew_tea("ginger"),
    brew_tea("lemon"),
    brew_tea("green"),
    brew_tea("black"),
    )
    
asyncio.run(main())