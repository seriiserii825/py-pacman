import os
from rich import print

from modules.getPackageFilePath import getPackageFilePath
user = os.getlogin()
def exportToFile(package_name, pacman):
    file_path = getPackageFilePath(pacman)
    with open(file_path, "a") as f:
        f.write(package_name + "\n")
    print(f"[bold green]Package {package_name} added to {file_path}[/bold green]")
