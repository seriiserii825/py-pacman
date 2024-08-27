import os
import subprocess
from rich import print

from modules.getAllInstalledPackages import getAllInstalledPackages
from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles
user = os.getlogin()
from config import CONFIG
def installDiff():
    packages = getAllInstalledPackages()
    all = packages["all"]
    print(f"[green]Total installed packages: {len(all)}")
    with open(CONFIG.DIFF_FILE_PATH, "r") as f:
        lines = f.readlines()
    diff_packages = [line.strip() for line in lines]
    print(f"[green]Total diff packages: {len(diff_packages)}")
    # get diff from all and diff_packages
    diff_packages = list(set(all) - set(diff_packages))
    if not diff_packages:
        diff_packages = list(set(diff_packages) - set(all))
    if not diff_packages:
        print("[red]No diff packages")
        return
    print(f"[green]Packages to install: {diff_packages}")
    for package in diff_packages:
        choice = input(f"Do you want to install {package} with pacman,y/n?: ")
        if choice == 'y':
            if package in packages["pacman"]:
                subprocess.run(f"sudo pacman -S {package}", shell=True)
            else:
                subprocess.run(f"yay -S {package}", shell=True)
        else:
            print(f"Skipping {package}")
    saveInstalledPackagesToFiles()
