import os
import subprocess

from modules.getAllInstalledPackages import getAllInstalledPackages
from modules.saveInstalledPackagesToFiles import saveInstalledPackagesToFiles
user = os.getlogin()
from config import CONFIG
def installDiff():
    pacman_command = f"pacman -Qe | awk '{{print $1}}' > {CONFIG.DIFF_FILE_PATH}"
    yay_command = f"pacman -Qm | awk '{{print $1}}' >> {CONFIG.DIFF_FILE_PATH}"
    subprocess.run(pacman_command, shell=True)
    subprocess.run(yay_command, shell=True)

    packages = getAllInstalledPackages()
    all = packages["all"]
    with open(CONFIG.DIFF_FILE_PATH, "r") as f:
        lines = f.readlines()
    diff_packages = [line.strip() for line in lines]
    diff_packages = list(set(diff_packages).difference(set(all)))
    print(f"diff_packages: {diff_packages}")
    if not diff_packages:
        print("[red]No packages to install")
        return
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
