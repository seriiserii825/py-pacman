from config import CONFIG
def getAllInstalledPackages():
    with open(CONFIG.INSTALLED_PACMAN_PATH, "r") as f:
        lines = f.readlines()
    # remove the newline character
    lines = [line.strip() for line in lines]
    packages_from_pacman = lines

    with open(CONFIG.INSTALLED_YAY_PATH) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    packages_from_yay = lines
    return {
            "pacman": packages_from_pacman,
            "yay": packages_from_yay,
            "all": packages_from_pacman + packages_from_yay
            }
