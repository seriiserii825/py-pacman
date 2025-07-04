import os


def updatePackages():
    pm = input("[green]Update pacman or yay packages? (p/y): ")
    if pm == "p":
        os.system("sudo pacman -Syu --noconfirm")
    else:
        os.system("yay -Syu --noconfirm")
