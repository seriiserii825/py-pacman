import os
from rich import print
from rich.panel import Panel

from modules.customTable import customTable
user = os.getlogin()
def diffInstalled():
    pacman_list = f"/home/{user}/xubuntu/pacman_list.txt"
    with open(pacman_list) as f:
        lines = f.readlines()
        packages_from_file = []
        for line in lines:
            line = line.strip()
            packages_from_file.append(line)
    
    command = f"pacman -Qe | awk '{{print $1}}' > temp.txt"
    os.system(command)
    with open("temp.txt") as f:
        lines = f.readlines()
        packages_from_system = []
        for line in lines:
            line = line.strip()
            packages_from_system.append(line)
        os.system("rm temp.txt")
    
    diff_from_system = set(packages_from_file) - set(packages_from_system)
    diff_from_file = set(packages_from_system) - set(packages_from_file)

    if len(diff_from_file) > 0:
        diff_from_file = list(diff_from_file)
        customTable("",["Non exists in file"], diff_from_file)
    else:
        print("[blue]No differences in file.")

    if len(diff_from_system) > 0:
        diff_from_system = list(diff_from_system)
        customTable("", ["Not installed in system"], diff_from_system)
    else:
        print("[blue]No differences in system.")
