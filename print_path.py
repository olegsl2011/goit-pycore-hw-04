import sys
from pathlib import Path
from colorama import Fore

def directory_structure_lines(directory, is_root=False, indent=0):
    lines = []
    if is_root:
        lines.append(f"{Fore.BLUE}{directory.name}/{Fore.RESET}")
    for item in directory.iterdir():
        if item.is_dir():
            lines.append(" " * indent + f"{Fore.BLUE}{item.name}/{Fore.RESET}")
            lines.extend(directory_structure_lines(item, indent=indent + 2))
        elif item.is_file():
            lines.append(" " * indent + f"{Fore.GREEN}{item.name}{Fore.RESET}")
    return lines

def get_directory_structure(path: str) -> str:
    path = Path(path)
    
    if path.exists():
        lines = directory_structure_lines(path, is_root=True, indent=2)
        return "\n".join(lines)
    else:
        raise FileNotFoundError(f"Directory '{path}' does not exist.")

if __name__ == "__main__":
    try:
        directory_structure = get_directory_structure("/Users/admin/Downloads/")
        print(directory_structure)
    except FileNotFoundError as e:
        print(e)