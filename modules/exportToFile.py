import os
from rich import print

from modules.getPackageFilePath import getPackageFilePath
user = os.getlogin()
def exportToFile(pacman):
    file_path = getPackageFilePath(pacman)
    command = f"pacman -Qe | awk '{{print $1}}' > {file_path}" if pacman else f"pacman -Qm | awk '{{print $1}}' > {file_path}"
    print(f"[green]Exporting to {file_path}...")
    os.system(command)
