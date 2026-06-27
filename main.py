import sys
from typing import Any
from code import InteractiveConsole

if sys.stdin.isatty() and hasattr(sys, "__interactivehook__"):
    sys.__interactivehook__()  # noqa


class PythonPlus(InteractiveConsole):
    def __init__(
        self, locals: dict[str, Any] | None = None, filename: str = "<console>"
    ) -> None:
        super().__init__(locals, filename)

        self._banner: str = (
            f"Python {sys.version} on {sys.platform}\n"
            'Type "help", "copyright", "credits" or "license" for more information.'
        )

    def interact(self, banner: str | None = None, exitmsg: str | None = None) -> None:
        _banner = banner if banner else self._banner
        return super().interact(_banner, exitmsg)


python_plus = PythonPlus()

python_plus.interact()
