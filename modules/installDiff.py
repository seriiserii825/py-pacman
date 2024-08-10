import os
user = os.getlogin()
def installDiff():
    pacman_list = f"/home/{user}/xubuntu/pacman_list.txt"
    with open(pacman_list) as f:
        lines = f.readlines()
        packages_from_file = []
        for line in lines:
            line = line.strip()
            packages_from_file.append(line)
    
    command = f"pacman -Qe | awk '{{print $1}}' > temp.txt"
    os.system(command)
    with open("temp.txt") as f:
        lines = f.readlines()
        packages_from_system = []
        for line in lines:
            line = line.strip()
            packages_from_system.append(line)
        os.system("rm temp.txt")
    
    diff = list(set(packages_from_system).symmetric_difference(set(packages_from_file)))
    command = f"sudo pacman -S {' '.join(diff)}"
    os.system(command)


