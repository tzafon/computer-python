"""Async Computer wrapper for cleaner API - protected from Stainless regeneration."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from ._client import AsyncComputer as AsyncTzafonClient
    from .types.action_result import ActionResult

__all__ = ["AsyncComputerWrapper"]


class AsyncComputerWrapper:
    """High-level async wrapper for computer automation with clean OOP API."""

    def __init__(self, client: AsyncTzafonClient, computer_id: str) -> None:
        self._client = client
        self.id = computer_id

    async def navigate(self, url: str) -> ActionResult:
        """Navigate to a URL."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "go_to_url", "url": url}}
        )

    async def type(self, text: str) -> ActionResult:
        """Type text."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "type", "text": text}}
        )

    async def click(self, x: int, y: int) -> ActionResult:
        """Click at coordinates."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "click", "x": x, "y": y}}
        )

    async def screenshot(self) -> ActionResult:
        """Take a screenshot."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "screenshot"}}
        )

    async def double_click(self, x: int, y: int) -> ActionResult:
        """Double-click at coordinates."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "double_click", "x": x, "y": y}}
        )

    async def right_click(self, x: int, y: int) -> ActionResult:
        """Right-click at coordinates."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "right_click", "x": x, "y": y}}
        )

    async def drag(self, from_x: int, from_y: int, to_x: int, to_y: int) -> ActionResult:
        """Drag from one position to another."""
        return await self._client.computers.execute_action(
            self.id,
            body={
                "action": {
                    "type": "drag",
                    "from_x": from_x,
                    "from_y": from_y,
                    "to_x": to_x,
                    "to_y": to_y,
                }
            },
        )

    async def hotkey(self, *keys: str) -> ActionResult:
        """Press a hotkey combination."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "hotkey", "keys": list(keys)}}
        )

    async def scroll(self, direction: str, amount: Optional[int] = None) -> ActionResult:
        """Scroll in a direction."""
        action: Dict[str, Any] = {"type": "scroll", "direction": direction}
        if amount is not None:
            action["amount"] = amount
        return await self._client.computers.execute_action(self.id, body={"action": action})

    async def wait(self, seconds: float) -> ActionResult:
        """Wait for a specified time."""
        return await self._client.computers.execute_action(
            self.id, body={"action": {"type": "wait", "seconds": seconds}}
        )

    async def terminate(self) -> None:
        """Terminate the computer session."""
        await self._client.computers.terminate(self.id)

    async def __aenter__(self) -> AsyncComputerWrapper:
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit - auto cleanup."""
        await self.terminate()

