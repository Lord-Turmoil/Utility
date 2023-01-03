import os
import re
from time import sleep


def rename(src):
    """
    Perform rename, this can be replaced for more patterns.
    :param src: source file name, no path
    :return: target file name if matched, None if no need
    """
    match_obj = re.search("S\d\dE\d\d", src, re.I)
    if match_obj:
        return match_obj.group() + src[src.rfind("."):]
    else:
        return None


def batch_rename(path):
    """
    :param path: root folder of files to batch rename
    :return: nothing
    """
    if not path.endswith("\\"):
        path += "\\"

    print("Searching...")
    for src in os.listdir(path):
        dest = rename(src)
        if dest:
            print(f"\tRename \"{src}\" to \"{dest}\"")
            os.rename(path + src, path + dest)


while True:
    print("------------- Copyright(C) Tony's Studio -------------")
    print("----------------- Batch Rename 1.0.0 -----------------")

    # Read folder and filename.
    path = input("Please enter the source folder: ").strip()
    if path == "quit":
        break

    batch_rename(path)

    ret = input("Continue? (Y/N) ").lower()
    if ret[0] != 'y':
        break
    os.system("cls")

print("Thanks for your using!")
sleep(0.8)

