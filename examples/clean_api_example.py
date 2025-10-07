"""Example of the clean OOP API wrapper."""

from tzafon import Tzafon, AsyncTzafon
import asyncio

# SYNC API
# ========

# Initialize client (automatically reads COMPUTER_API_KEY from env)
client = Tzafon()

# Example 1: Using context manager (auto-cleanup)
with client.create(kind="browser") as computer:
    computer.navigate("https://google.com")
    computer.type("Hello World")
    computer.click(100, 200)
    screenshot = computer.screenshot()
    print(f"Screenshot result: {screenshot.status}")

# Example 2: Manual management
computer = client.create(kind="browser")
try:
    computer.navigate("https://example.com")
    computer.type("Testing")
    computer.screenshot()
finally:
    computer.terminate()

# Example 3: Advanced actions
with client.create(kind="browser") as computer:
    computer.navigate("https://github.com")
    computer.wait(2.0)  # Wait 2 seconds
    computer.scroll("down", amount=500)
    computer.hotkey("ctrl", "f")  # Ctrl+F
    computer.type("search term")
    computer.double_click(300, 400)
    computer.right_click(500, 600)
    computer.drag(100, 100, 200, 200)


# ASYNC API
# =========

async def async_example():
    """Async version of the clean API."""
    client = AsyncTzafon()  # automatically reads COMPUTER_API_KEY from env
    
    # Using async context manager
    async with client.create(kind="browser") as computer:
        await computer.navigate("https://google.com")
        await computer.type("Hello World")
        await computer.click(100, 200)
        screenshot = await computer.screenshot()
        print(f"Screenshot result: {screenshot.status}")

# Run async example
# asyncio.run(async_example())
