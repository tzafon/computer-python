"""Clean OOP API for Tzafon browser automation."""

from tzafon import Computer, AsyncComputer

# Initialize client (auto-reads COMPUTER_API_KEY from env)
client = Computer()

# Context manager (auto-cleanup)
with client.create(kind="browser") as computer:
    computer.navigate("https://google.com")
    computer.type("Hello World")
    computer.click(100, 200)
    screenshot = computer.screenshot()
    print(f"Screenshot: {screenshot.result['screenshot_url']}")

# All available actions
with client.create(kind="browser") as computer:
    computer.navigate("https://github.com")
    computer.wait(2.0)
    computer.scroll("down", amount=500)
    computer.hotkey("ctrl", "f")
    computer.type("search term")
    computer.click(100, 200)
    computer.double_click(300, 400)
    computer.right_click(500, 600)
    computer.drag(100, 100, 200, 200)


# Async version
async def async_example():
    client = AsyncComputer()
    async with client.create(kind="browser") as computer:
        await computer.navigate("https://google.com")
        await computer.type("Hello World")
        screenshot = await computer.screenshot()
        print(f"Screenshot: {screenshot.result['screenshot_url']}")


# import asyncio
# asyncio.run(async_example())
