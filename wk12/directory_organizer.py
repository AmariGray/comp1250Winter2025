"""
This is a directory organizer module that allows a user
to CRUD directories

User can add, rename, delete, and view contents of a directory
"""
import os, re
import sys


def add():
    name_of_directory = input("Enter a directory name")
    if not os.path.exists(name_of_directory):
        os.mkdir(name_of_directory)
    else:
        print(name_of_directory, "already exists", file=sys.stderr)

def rename():
    source_directory = input("Enter the source directory")
    destination_directory = input("Enter the destination directory")
    if not os.path.exists(source_directory):
        print(source_directory, "does not exists, therefor we cannot rename the directory")
    else:
        os.rename(source_directory, destination_directory)

def view():
    directory = input("Enter a path or name of a directory")

    if os.path.exists(directory):
        print("All files and folders of the directory", directory,
              "is", "\n".join(os.listdir(directory)))
    else:
        print(directory, "does not exist", file=sys.stderr)

def delete():
    directory = input("Enter a path or name of a directory")

    if os.path.exists(directory):
        os.rmdir(directory)
        print(directory, "was successfully removed")
    else:
        print(directory, "does not exist!")


options = ["(A)dd directory", "(D)elete directory",
           "(V)iew directory", "(R)ename directory",
           "(Q)uit"]


def validate_choice(choice):
    pattern = r"[advrq]"
    match = re.match(pattern=pattern, string=choice[0], flags=re.I)

    if match:
        return True
    return False


def main():
    print("Welcome to our Directory CRUD app")
    while True:
        print("What would you like to do?")
        choice = input("\n".join(options) + "\n")
        if validate_choice(choice):
            # based on choice, call on any of the methods above
            # you may need to add method arguments to methods
            # fill out the bodies of the methods so they actually accomplish their function (add, actually adds, and etc)
            if choice[0].lower() == "a":
                add()
            elif choice[0].lower() == "d":
                delete()
            elif choice[0].lower() == "v":
                view()
            elif choice[0].lower() == "r":
                rename()
            else:
                break

        else:
            print(f"Error! {choice} is invalid", file=sys.stderr)


if __name__ == '__main__':
    main()
