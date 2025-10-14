"""RotorHazard plugin: Announce heat number at race start using documented RHAPI.

This plugin listens for the race start event and triggers a UI message to speak:
"Heat <number> started".

It uses only the documented RHAPI calls:
- Event binding: rhapi.events.on(Evt.<...>, handler) with Evt imported from eventmanager
- UI speech: rhapi.ui.message_speak(message)
- Current heat id: rhapi.race.heat (int or None)
"""

from __future__ import annotations

from typing import Any

from eventmanager import Evt


def _on_race_start(_args: dict, rhapi: Any) -> None:
    """Announce heat number via the UI TTS when a race starts."""
    heat_id = getattr(rhapi.race, "heat", None)
    if isinstance(heat_id, int) and heat_id > 0:
        rhapi.ui.message_speak(f"Heat {heat_id} started")
    else:
        rhapi.ui.message_speak("Heat started")


def initialize(rhapi: Any) -> None:
    """RotorHazard plugin entry point."""
    rhapi.events.on(Evt.RACE_START, lambda args: _on_race_start(args, rhapi))
