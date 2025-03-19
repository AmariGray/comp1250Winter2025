"""
This is a directory organizer module that allows a user
to CRUD directories

User can add, rename, delete, and view contents of a directory
"""
import os, re
import sys


def add():
    pass
def rename():
    pass
def view():
    pass
def delete():
    pass

options = ["(A)dd directory", "(D)elete directory",
           "(V)iew directory", "(R)ename directory"]


def validate_choice(choice):
    pattern = r"[advr]"
    match = re.match(pattern=pattern, string=choice[0], flags=re.I)

    if match:
        return True
    return False

def main():
    print("Welcome to our Directory CRUD app")
    print("What would you like to do?")
    choice = input("\n".join(options))
    if validate_choice(choice):
        # based on choice, call on any of the methods above
        # you may need to add method arguments to methods
        # fill out the bodies of the methods so they actually accomplish their function (add, actually adds, and etc)
        pass
    else:
        print(f"Error! {choice} is invalid", file=sys.stderr)

if __name__ == '__main__':
    main()
