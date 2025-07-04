import subprocess

from rich import print

from config import CONFIG


def saveInstalledPackagesToFiles(sync=False):
    pacman_command = f"pacman -Qe | awk '{{print $1}}' > {CONFIG.INSTALLED_PACMAN_PATH}"
    yay_command = f"pacman -Qm | awk '{{print $1}}' > {CONFIG.INSTALLED_YAY_PATH}"
    subprocess.run(pacman_command, shell=True)
    subprocess.run(yay_command, shell=True)
    if sync:
        pacman_command = f"pacman -Qe | awk '{{print $1}}' > {CONFIG.DIFF_FILE_PATH}"
        yay_command = f"pacman -Qm | awk '{{print $1}}' >> {CONFIG.DIFF_FILE_PATH}"
        subprocess.run(pacman_command, shell=True)
        subprocess.run(yay_command, shell=True)
        print("[green]Installed packages saved to files and synced with diff file")
    else:
        print("[green]Installed packages saved to files")
