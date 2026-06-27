import os


class Clear:
    def __repr__(self) -> str:
        clear_cmd = "cls" if os.name == "nt" else "clear"
        os.system(clear_cmd)
        return ""


class ListDir:
    def __repr__(self) -> str:
        list_dir_cmd = "dir" if os.name == "nt" else "ls"
        os.system(list_dir_cmd)
        return ""


clear = Clear()
ls = ListDir()
