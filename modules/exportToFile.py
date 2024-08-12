import os
from rich import print
user = os.getlogin()
def exportToFile(pacman):
    file_name = "pacman_list.txt" if pacman else "yay_list.txt"
    file_path = f"/home/{user}/xubuntu/{file_name}"
    command = f"pacman -Qe | awk '{{print $1}}' > {file_path}" if pacman else f"pacman -Qm | awk '{{print $1}}' > {file_path}"
    print(f"[green]Exporting to /home/{user}/xubuntu/{file_name}")
    os.system(command)
