<!-- PLUGIN BADGES -->
[![RHFest][rhfest-shield]][rhfest-url]

# Heat Number Announcer (RotorHazard Plugin)

This plugin announces "Heat <number> started" via the UI message_speak mechanism when a race starts.

It uses RHAPI:
- Event binding: rhapi.events.on(Evt.RACE_START, handler) with Evt imported from eventmanager
- Speech: rhapi.ui.message_speak(message)
- Heat number: rhapi.race.heat (int or None)


# Development

See: [DEVELOPMENT.md](DEVELOPMENT.md)
