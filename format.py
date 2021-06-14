import glob
from os import chdir, system

files = ["./app/auth/__init__.py", "./app/auth/views.py"]


def add_files():
    chdir("./app")
    for file in glob.glob("*.py"):
        files.append(file)


def format():
    for i in files:
        system(f"autopep8 --in-place --aggressive {i}")


if __name__ == "__main__":
    add_files()
    format()
    print("All done!")
