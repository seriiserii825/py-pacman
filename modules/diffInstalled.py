import os
from rich import print
from rich.panel import Panel

from modules.customTable import customTable
from modules.exportToFile import exportToFile
from modules.installPackage import installPackage
user = os.getlogin()
def diffInstalled(pacman = True):
    file_name = "pacman_list.txt" if pacman else "yay_list.txt"
    packages__list = f"/home/{user}/xubuntu/{file_name}"
    packages_from_file = []
    packages_from_system = []
    with open(packages__list) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            packages_from_file.append(line)
    
    command = "pacman -Qe | awk '{print $1}' > temp.txt" if pacman else "pacman -Qm | awk '{{print $1}}' > temp.txt"
    os.system(command)
    with open("temp.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            packages_from_system.append(line)
        os.system("rm temp.txt")
    
    diff_from_system = set(packages_from_file) - set(packages_from_system)
    diff_from_file = set(packages_from_system) - set(packages_from_file)

    if len(diff_from_file) > 0:
        diff_from_file = list(diff_from_file)
        customTable("",["Non exists in file"], diff_from_file)
        write_to_file = input("Write to file? (y/n): ")
        if write_to_file:
            with open(packages__list, "a") as f:
                for line in diff_from_file:
                    f.write(line + "\n")
            print(Panel(f"[green]File {packages__list} created with {len(diff_from_file)} lines."))
        exportToFile(pacman)
    else:
        print("[blue]No differences in file.")

    if len(diff_from_system) > 0:
        diff_from_system = list(diff_from_system)
        customTable("", ["Not installed in system"], diff_from_system)
        install = input("Install? (y/n): ")
        if install:
            for package in diff_from_system:
                install_one = input(f"Install {package}? (y/n): ")
                if install_one:
                    installPackage(pacman, package)
    else:
        print("[blue]No differences in system.")
