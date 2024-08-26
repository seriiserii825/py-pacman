import os
from rich import print
from rich.panel import Panel
from appSettings import appSettings
PACMAN_SEARCH_PATH = appSettings()["SEARCH_PACMAN_PATH"]
YAY_SEARCH_PATH = appSettings()["SEARCH_YAY_PATH"]
def searchPackage():
    package = input("Enter package name: ")
    if not package:
        print(Panel("Package name is required!"))
        return
    os.system(f"pacman -Ss {package} > {PACMAN_SEARCH_PATH}")
    os.system(f"yay -Ss {package} > {YAY_SEARCH_PATH}")
