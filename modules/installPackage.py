import os

from modules.exportToFile import exportToFile
def installPackage(pacman = True, prop_package = ''):
    if prop_package:
        package = prop_package
    else:
        package = input("Enter package name: ")
    if pacman:
        os.system(f"sudo pacman -S {package}")
        exportToFile(pacman)
    else:
        os.system(f"yay -S {package}")
        exportToFile(pacman)

