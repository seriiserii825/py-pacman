import os
from rich import print
from rich.panel import Panel
from appSettings import appSettings
PACMAN_SEARCH_PATH = appSettings()["SEARCH_PACMAN_PATH"]
YAY_SEARCH_PATH = appSettings()["SEARCH_YAY_PATH"]
print(f"Pacman search path: {PACMAN_SEARCH_PATH}")
print(f"Yay search path: {YAY_SEARCH_PATH}")
def searchPackage():
    package = input("Enter package name: ")
    if not package:
        print(Panel("Package name is required!"))
        return
    os.system(f"sudo pacman -Ss {package} > {PACMAN_SEARCH_PATH}")
    os.system(f"yay -Ss {package} > {YAY_SEARCH_PATH}")
    print(Panel("Pacman", title="Pacman"))
    os.system(f"bat {PACMAN_SEARCH_PATH}")
    print(Panel("Yay", title="Yay"))
    os.system(f"bat {YAY_SEARCH_PATH}")
