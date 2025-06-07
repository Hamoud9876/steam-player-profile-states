from db.seed import seed
import asyncio


def main():
    asyncio.run(seed())


main()
