import os
from rich import print
user = os.getlogin()
def exportToFile(package = ''):
    if package != '':
        command = f"echo {package} >> /home/{user}/xubuntu/pacman_list.txt"
        print(f"[green]Exporting to /home/{user}/xubuntu/pacman_list.txt")
        os.system(command)
        exportToFile()
    else:
        command = f"pacman -Qe | awk '{{print $1}}' > /home/{user}/xubuntu/pacman_list.txt"
        print(f"[green]Exporting to /home/{user}/xubuntu/pacman_list.txt")
        os.system(command)
