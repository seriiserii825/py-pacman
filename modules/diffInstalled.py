import os
from rich import print

from modules.customTable import customTable
from modules.exportToFile import exportToFile
from modules.getIgnoredPackagesList import getIgnoredPackagesList
from modules.getPackageFilePath import getPackageFilePath
from modules.installPackage import installPackage
user = os.getlogin()
def diffInstalled(pacman = True):
    packages__list = getPackageFilePath(pacman)
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
        ignored_packages = getIgnoredPackagesList()
        diff_from_file = [package for package in diff_from_file if package not in ignored_packages]
        diff_from_file = sorted(diff_from_file)
        customTable("",["Non exists in file"], diff_from_file)
        write_to_file = input("Write to file? (y/n): ")
        if write_to_file == 'y':
            with open(packages__list, "a") as f:
                for line in diff_from_file:
                    f.write(line + "\n")
            exportToFile(pacman)
    else:
        print("[blue]No differences in file.")

    if len(diff_from_system) > 0:
        diff_from_system = list(diff_from_system)
        ignored_packages = getIgnoredPackagesList()
        diff_from_system = [package for package in diff_from_system if package not in ignored_packages]
        diff_from_system = sorted(diff_from_system)
        customTable("", ["Not installed in system"], diff_from_system)
        install = input("Install? (y/n): ")
        if install == 'y':
            for package in diff_from_system:
                install_one = input(f"Install {package}? (y/n): ")
                if install_one == 'y':
                    installPackage(pacman, package)
    else:
        print("[blue]No differences in system.")
