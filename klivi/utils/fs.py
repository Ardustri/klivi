import os
from typing import IO


def write_file(filename: str, content: str, mode: str = "w") -> IO:
    """Save content to a file, overwriting it by default."""
    with open(filename, mode) as file:
        file.write(content)
    return file


def read_file(filename: str, mode: str = "r") -> str:
    """Read content from a file."""
    with open(filename, mode) as file:
        file_content = file.read()
    return file_content


def exist(name: str) -> bool:
    """Check whether a give path exists."""
    return bool(os.path.exists(name))


def mkdir(folder_name: str) -> None:
    """Create a directory at the given location if does not exist."""
    if exist(folder_name):
        print("The folder is already exist")
        return 

    os.mkdir(folder_name)


def rmdir(folder_name: str) -> None:
    """Remove a directory at the given location if does exist."""
    if not exist(folder_name):
        print("The folder does not exist")
        return
    
    os.rmdir(folder_name)

