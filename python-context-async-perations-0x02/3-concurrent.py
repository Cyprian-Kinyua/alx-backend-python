import aiosqlite
import asyncio

# ✅ Async function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("\n📄 All Users:")
            for user in users:
                print(user)

# ✅ Async function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            older_users = await cursor.fetchall()
            print("\n📄 Users Over 40:")
            for user in older_users:
                print(user)

# ✅ Function to run both queries concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# ✅ Run it all
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
