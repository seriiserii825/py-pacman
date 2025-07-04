import os

from pyfzf.pyfzf import FzfPrompt
from rich import print

from config import CONFIG
from modules.searchPackage import PACMAN_SEARCH_PATH, YAY_SEARCH_PATH

fzf = FzfPrompt()


class Package:
    def __init__(self):
        self.installed_pacman = []
        self.installed_yay = []
        self.searched_pacman = []
        self.searched_yay = []
        self.diff_pacman = []
        self.diff_yay = []
        os.system(f"touch {CONFIG.DIFF_PACMAN_PATH}")
        os.system(f"touch {CONFIG.DIFF_YAY_PATH}")

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
            self.addPackageToFile(package, CONFIG.INSTALLED_PACMAN_PATH)
            self.uniqueFile(CONFIG.INSTALLED_PACMAN_PATH)
            self.sortFile(CONFIG.INSTALLED_PACMAN_PATH)
        else:
            package = fzf.prompt(self.searched_yay)
            package = package[0].split(" ")[0]
            package = package.split("/")[1]
            command = f"yay -S {package} --noconfirm"
            os.system(command)
            self.addPackageToFile(package, CONFIG.INSTALLED_YAY_PATH)
            self.uniqueFile(CONFIG.INSTALLED_YAY_PATH)
            self.sortFile(CONFIG.INSTALLED_YAY_PATH)

    def addPackageToFile(self, package, file_path):
        with open(file_path, "a") as f:
            f.write(package + "\n")

    def sortFile(self, file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
        with open(file_path, "w") as f:
            lines.sort()
            for line in lines:
                f.write(line)

    def uniqueFile(self, file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
        with open(file_path, "w") as f:
            lines = list(set(lines))
            for line in lines:
                f.write(line)

    def removeLinesWithEmptySpaceAtStart(self, file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()
        with open(file_path, "w") as f:
            for line in lines:
                print(f"line: {line}")
                if not line.startswith(" "):
                    f.write(line)

    def getPackagesFromPacmanFile(self):
        with open(CONFIG.INSTALLED_PACMAN_PATH, "r") as f:
            self.installed_pacman = f.read().splitlines()

    def getPacmanPackages(self):
        return self.installed_pacman

    def getPackagesFromYayFile(self):
        with open(CONFIG.INSTALLED_YAY_PATH, "r") as f:
            self.installed_yay = f.read().splitlines()

    def getPackagesFromDiffPacmanFile(self):
        with open(CONFIG.DIFF_PACMAN_PATH, "r") as f:
            self.diff_pacman = f.read().splitlines()

    def getPackageFromDiffYayFile(self):
        with open(CONFIG.DIFF_YAY_PATH, "r") as f:
            self.diff_yay = f.read().splitlines()

    def getYayPackages(self):
        return self.installed_yay

    def removePackageFromPacmanFile(self, package):
        with open(CONFIG.INSTALLED_PACMAN_PATH, "r") as f:
            lines = f.readlines()
        with open(CONFIG.INSTALLED_PACMAN_PATH, "w") as f:
            for line in lines:
                if line.strip("\n") != package:
                    f.write(line)

    def removePackageFromYayFile(self, package):
        with open(CONFIG.INSTALLED_YAY_PATH, "r") as f:
            lines = f.readlines()
        with open(CONFIG.INSTALLED_YAY_PATH, "w") as f:
            for line in lines:
                if line.strip("\n") != package:
                    f.write(line)

    def showInstalledPackages(self):
        self.getPackagesFromPacmanFile()
        self.getPackagesFromYayFile()
        package_type = input("Show pacman or yay packages? (p/y): ")
        if package_type == "p":
            print("[green]Pacman =====================")
            os.system(f"bat {CONFIG.INSTALLED_PACMAN_PATH}")
        else:
            print("[blue]Yay =====================")
            os.system(f"bat {CONFIG.INSTALLED_YAY_PATH}")

    def removePackageFromDiffPacmanFile(self, package):
        with open(CONFIG.DIFF_PACMAN_PATH, "r") as f:
            lines = f.readlines()
        with open(CONFIG.DIFF_PACMAN_PATH, "w") as f:
            for line in lines:
                if line.strip("\n") != package:
                    f.write(line)

    def installDiffPacmanPackages(self):
        self.getPackagesFromDiffPacmanFile()
        if self.diff_pacman == []:
            print("[red]No diff packages to install")
            return
        package = fzf.prompt(self.diff_pacman)
        command = f"sudo pacman -S {package}"
        os.system(command)
        self.addPackageToFile(package, CONFIG.INSTALLED_PACMAN_PATH)
        self.sortFile(CONFIG.INSTALLED_PACMAN_PATH)
        self.removePackageFromDiffPacmanFile(package)

    def removePackageFromDiffYayFile(self, package):
        with open(CONFIG.DIFF_YAY_PATH, "r") as f:
            lines = f.readlines()
        with open(CONFIG.DIFF_YAY_PATH, "w") as f:
            for line in lines:
                if line.strip("\n") != package:
                    f.write(line)

    def installDiffYayPackages(self):
        self.getPackageFromDiffYayFile()
        if self.diff_yay == []:
            print("[red]No diff packages to install")
            return
        package = fzf.prompt(self.diff_yay)
        command = f"yay -S {package}"
        os.system(command)
        self.addPackageToFile(package, CONFIG.INSTALLED_YAY_PATH)
        self.sortFile(CONFIG.INSTALLED_YAY_PATH)
        self.removePackageFromDiffYayFile(package)
