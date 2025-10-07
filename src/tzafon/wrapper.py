"""Custom Computer wrapper for cleaner API - protected from Stainless regeneration."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from ._client import Computer as TzafonClient
    from .types.action_result import ActionResult

__all__ = ["ComputerWrapper"]


class ComputerWrapper:
    """High-level wrapper for computer automation with clean OOP API."""

    def __init__(self, client: TzafonClient, computer_id: str) -> None:
        self._client = client
        self.id = computer_id

    def navigate(self, url: str) -> ActionResult:
        """Navigate to a URL."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "go_to_url", "url": url}}
        )

    def type(self, text: str) -> ActionResult:
        """Type text."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "type", "text": text}}
        )

    def click(self, x: int, y: int) -> ActionResult:
        """Click at coordinates."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "click", "x": x, "y": y}}
        )

    def screenshot(self) -> ActionResult:
        """Take a screenshot."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "screenshot"}}
        )

    def double_click(self, x: int, y: int) -> ActionResult:
        """Double-click at coordinates."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "double_click", "x": x, "y": y}}
        )

    def right_click(self, x: int, y: int) -> ActionResult:
        """Right-click at coordinates."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "right_click", "x": x, "y": y}}
        )

    def drag(self, from_x: int, from_y: int, to_x: int, to_y: int) -> ActionResult:
        """Drag from one position to another."""
        return self._client.computers.execute_action(
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

    def hotkey(self, *keys: str) -> ActionResult:
        """Press a hotkey combination."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "hotkey", "keys": list(keys)}}
        )

    def scroll(self, direction: str, amount: Optional[int] = None) -> ActionResult:
        """Scroll in a direction."""
        action: Dict[str, Any] = {"type": "scroll", "direction": direction}
        if amount is not None:
            action["amount"] = amount
        return self._client.computers.execute_action(self.id, body={"action": action})

    def wait(self, seconds: float) -> ActionResult:
        """Wait for a specified time."""
        return self._client.computers.execute_action(
            self.id, body={"action": {"type": "wait", "seconds": seconds}}
        )

    def terminate(self) -> None:
        """Terminate the computer session."""
        self._client.computers.terminate(self.id)

    def __enter__(self) -> ComputerWrapper:
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit - auto cleanup."""
        self.terminate()

