from os import system, chdir
import glob

files = ["app/auth/__init__.py", "app/auth/views.py"]


def add_files():
    chdir("./app")
    for file in glob.glob("*.py"):
        files.append(file)


def check_format():
    for i in files:
        system(f"pycodestyle --show-source --show-pep8 --format=default {i}")


if __name__ == "__main__":
    add_files()
    check_format()
    print("All done!")
