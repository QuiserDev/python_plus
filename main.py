import os
import sys
import re
from typing import Any, Callable
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

        self.cmd_map: dict[str, Callable] = dict()

    def interact(self, banner: str | None = None, exitmsg: str | None = None) -> None:
        _banner = banner if banner else self._banner
        return super().interact(_banner, exitmsg)

    def push(self, line: str) -> bool:
        pattern = r"(?:-[\w]+)|(?:'[^']*')|(?:\"[^\"]*\")|(?:\S+)"
        args = re.findall(pattern, line)
        for cmd, func in self.cmd_map.items():
            if args and args[0] == cmd:
                return func(*args[1:])

        return super().push(line)

    def register(self, cmd: str):
        def inner(func: Callable):
            self.cmd_map[cmd] = func

        return inner


python_plus = PythonPlus()


@python_plus.register("ls")
def ls_func(_path: str = ""):
    os.system(" ".join(("ls", _path)))


python_plus.interact()
