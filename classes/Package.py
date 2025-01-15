from config import CONFIG


class Package():
    def __init__(self):
        self.installed_pacman = []
        self.installed_yay = []
        self.diff = []
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

