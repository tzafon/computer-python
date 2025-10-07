# Tzafon Python SDK - Clean Wrapper API

Beautiful OOP wrapper for the Tzafon browser automation API.

## Setup

Set your API key as an environment variable:
```bash
export COMPUTER_API_KEY=wpk_QUCIth7oNvAei4hV2i1c9uDl5yLaVmRJ
```

## Usage

### Basic Example

```python
from tzafon import Tzafon

client = Tzafon()  # Automatically uses COMPUTER_API_KEY env var

# Using context manager (auto-cleanup)
with client.create(kind="browser") as computer:
    computer.navigate("https://google.com")
    computer.type("Hello World")
    computer.click(100, 200)
    screenshot = computer.screenshot()
    print(f"Status: {screenshot.status}")
```

### Manual Management

```python
from tzafon import Tzafon

client = Tzafon()
computer = client.create(kind="browser")

try:
    computer.navigate("https://example.com")
    computer.type("Testing")
    screenshot = computer.screenshot()
finally:
    computer.terminate()
```

### All Available Actions

```python
with client.create(kind="browser") as computer:
    # Navigate
    computer.navigate("https://github.com")
    
    # Wait
    computer.wait(2.0)  # seconds
    
    # Scroll
    computer.scroll("down", amount=500)
    
    # Click actions
    computer.click(100, 200)
    computer.double_click(300, 400)
    computer.right_click(500, 600)
    
    # Drag
    computer.drag(from_x=100, from_y=100, to_x=200, to_y=200)
    
    # Keyboard
    computer.type("search term")
    computer.hotkey("ctrl", "f")  # Ctrl+F
    computer.hotkey("cmd", "c")   # Cmd+C (Mac)
    
    # Screenshot
    screenshot = computer.screenshot()
```

### Async API

```python
from tzafon import AsyncTzafon

async def main():
    client = AsyncTzafon()
    
    async with client.create(kind="browser") as computer:
        await computer.navigate("https://google.com")
        await computer.type("Hello World")
        await computer.click(100, 200)
        screenshot = await computer.screenshot()

import asyncio
asyncio.run(main())
```

## Action Types

The wrapper supports all backend action types:
- `navigate(url)` - Navigate to URL (uses `go_to_url` backend action)
- `type(text)` - Type text
- `click(x, y)` - Click at coordinates
- `screenshot()` - Take screenshot
- `double_click(x, y)` - Double-click
- `right_click(x, y)` - Right-click
- `drag(from_x, from_y, to_x, to_y)` - Drag
- `hotkey(*keys)` - Press hotkey combination
- `scroll(direction, amount=None)` - Scroll
- `wait(seconds)` - Wait

## Original SDK Methods Still Available

You can still use the original Stainless-generated methods:

```python
from tzafon import Tzafon

client = Tzafon()

# Original API still works
response = client.computers.create(kind="browser")
client.computers.execute_action(
    response.id,
    body={"action": {"type": "go_to_url", "url": "https://google.com"}}
)
client.computers.terminate(response.id)
```

## Files Protected from Stainless Regeneration

Custom wrapper files are listed in `.stainless-ignore`:
- `src/tzafon/wrapper.py`
- `src/tzafon/async_wrapper.py`
- `src/tzafon/client_extensions.py`

These won't be overwritten when Stainless regenerates the SDK.

