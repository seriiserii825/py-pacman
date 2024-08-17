import os
def removePackageFromFile(file, packageName):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file + '.tmp', 'w') as f:
        for line in lines:
            if packageName not in line:
                f.write(line)
            else:
                print(f"Removed {packageName} from {file}")
    os.rename(file + '.tmp', file)
    os.remove(file)
