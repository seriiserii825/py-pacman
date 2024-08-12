import os
def installPackage(pacman = True):
    package = input("Enter package name: ")
    if pacman:
        os.system(f"sudo pacman -S {package}")
    else:
        os.system(f"yay -S {package}")

