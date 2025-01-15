import os
from rich import print
from config import CONFIG
from pyfzf.pyfzf import FzfPrompt
from modules.searchPackage import PACMAN_SEARCH_PATH, YAY_SEARCH_PATH
fzf = FzfPrompt()


class Package():
    def __init__(self):
        self.installed_pacman = []
        self.installed_yay = []
        self.searched_pacman = []
        self.searched_yay = []
        self.diff = []

    def searchPackage(self):
        package = input("Enter package name: ")
        if not package:
            print("Package name is required!")
            return
        os.system(f"sudo pacman -Ss {package} > {PACMAN_SEARCH_PATH}")
        os.system(f"yay -Ss {package} > {YAY_SEARCH_PATH}")
        self.removeLinesWithEmptySpaceAtStart(PACMAN_SEARCH_PATH)
        self.removeLinesWithEmptySpaceAtStart(YAY_SEARCH_PATH)
        self.searched_pacman = open(PACMAN_SEARCH_PATH, "r").read().split("\n")
        self.searched_yay = open(YAY_SEARCH_PATH, "r").read().split("\n")
        print("[green]Pacman =====================")
        os.system(f"cat {PACMAN_SEARCH_PATH}")
        print("[blue]Yay =====================")
        os.system(f"cat {YAY_SEARCH_PATH}")

        choose = input("Install in pacman or yay? (p/y): ")
        if choose == "p":
            package = fzf.prompt(self.searched_pacman)
            package = package[0].split(" ")[0]
            package = package.split("/")[1]
            command = f"sudo pacman -S --noconfirm {package}"
            os.system(command)
        else:
            package = fzf.prompt(self.searched_yay)
            package = package[0].split(" ")[0]
            package = package.split("/")[1]
            command = f"yay -S {package}"
            os.system(command)

    def removeLinesWithEmptySpaceAtStart(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        with open(file_path, 'w') as f:
            for line in lines:
                print(f'line: {line}')
                if not line.startswith(" "):
                    f.write(line)

    def getPackagesFromPacmanFile(self):
        with open(CONFIG.INSTALLED_PACMAN_PATH, 'r') as f:
            self.installed_pacman = f.read().splitlines()
    def getPacmanPackages(self):
        return self.installed_pacman

    def getPackagesFromYayFile(self):
        with open(CONFIG.INSTALLED_YAY_PATH, 'r') as f:
            self.installed_yay = f.read().splitlines()
            
    def getYayPackages(self):
        return self.installed_yay

    def removePackageFromPacmanFile(self, package):
        with open(CONFIG.INSTALLED_PACMAN_PATH, 'r') as f:
            lines = f.readlines()
        with open(CONFIG.INSTALLED_PACMAN_PATH, 'w') as f:
            for line in lines:
                if line.strip("\n") != package:
                    f.write(line)

    def removePackageFromYayFile(self, package):
        with open(CONFIG.INSTALLED_YAY_PATH, 'r') as f:
            lines = f.readlines()
        with open(CONFIG.INSTALLED_YAY_PATH, 'w') as f:
            for line in lines:
                if line.strip("\n") != package:
                    f.write(line)

