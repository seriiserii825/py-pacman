import os
def showPackages(pacman = True):
    if pacman:
        os.system(f"pacman -Qe | awk '{{print $1}}' | less")
    else:
        # find packages installed with yay
        os.system(f"pacman -Qm | awk '{{print $1}}' | less")
