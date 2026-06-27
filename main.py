import os


class Clear:
    def __repr__(self) -> str:
        clear_cmd = "cls" if os.name == "nt" else "clear"
        os.system(clear_cmd)
        return ""


clear = Clear()
