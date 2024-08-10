import os
from rich import print
user = os.getlogin()
def exportToFile():
    command = f"pacman -Qe | awk '{{print $1}}' > /home/{user}/xubuntu/pacman_list.txt"
    print(f"[green]Exporting to /home/{user}/xubuntu/pacman_list.txt")
    os.system(command)
