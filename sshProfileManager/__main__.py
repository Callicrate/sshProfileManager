import os
import sys
from os import listdir
from os.path import isfile, join
from os.path import expanduser

enabled_files = []
base_files = []



def main(*_):

    engine()


def print_status_and_exit():
    print(f"--------------------------")
    print(f"SSH PROFILE MANAGER STATUS")
    print(f"--------------------------")
    print(f"All Profiles:")
    print(*base_files)
    print()
    print(f"Enabled Profiles:  ")
    print(*enabled_files)
    sys.exit(0)


def engine():
    home = expanduser("~")
    mypath = home + "/.ssh/config.d/"
    all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    # sort the files into buckets
    for file in all_files:
        if file.endswith(".enabled"):
            enabled_files.append(file[:-8])
        else:
            base_files.append(file)

    # if there are no args, then print out the filenames and exit
    if len(sys.argv) == 1:
        print_status_and_exit()

    # check that all arguments are legitimate, if not then print the status
    for argument in sys.argv[1:]:
        if argument not in base_files:
            print(f"ERROR: {argument} is not a valid profile")
            sys.exit(1)

    # disable everything by deleting all .enabled files
    for file in enabled_files:
        file_path = mypath + file + ".enabled"
        os.unlink(file_path)

    # second we enable anything that is listed as an arg
    enabled_files.clear()
    for file in sys.argv[1:]:
        file_path = mypath+file
        link_path = file_path + ".enabled"
        os.symlink(file_path, link_path)
        enabled_files.append(file)

    print_status_and_exit()


if __name__ == '__main__':
    main()
