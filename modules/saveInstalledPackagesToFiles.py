import subprocess
from config import CONFIG
def saveInstalledPackagesToFiles():
    pacman_command = f"pacman -Qe | awk '{{print $1}}' > {CONFIG.INSTALLED_PACMAN_PATH}"
    print(f"pacman_command: {pacman_command}")
    yay_command = f"pacman -Qm | awk '{{print $1}}' > {CONFIG.INSTALLED_YAY_PATH}"
    print(f"yay_command: {yay_command}")
    subprocess.run(pacman_command, shell=True)
    subprocess.run(yay_command, shell=True)
