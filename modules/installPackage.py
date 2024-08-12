import os
def installPackage(pacman = True, prop_package = ''):
    if prop_package:
        package = prop_package
    else:
        package = input("Enter package name: ")
    if pacman:
        os.system(f"sudo pacman -S {package}")
    else:
        os.system(f"yay -S {package}")

