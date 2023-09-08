import sys
import os
import argparse
import re

# import datetime
# too lazy xd


def parsing_args():
    global argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-a")
    parser.add_argument("-n")
    parser.add_argument("-t")
    return parser.parse_args()


# ----------------------
# files:
# projects.txt - list of all projects with path
# active.txt - active project with path
# folder "commits" - with commits in txt files main.py.txt fx
# crp - create project
# addf - add file
# addp - add project
# sc - search commit
# addc - add commit
# lc - list commits
# -- use of this --
# python pygit.py
# crp name - create project
# addf name - addfile
# actp name - activate project
# lc file - list commits of a file
# sc file text - search commit where "text" -> id of commit
# retc idcommit - return version of file in commit with id
# addc file change - add commit to file with what changes
# delf file - delete file and it's commits
# delc idcommit - delete commit by it's id
# delp name - delete project by it's name
# -----------------
# 1 - func; 2 - file/name 3 - change/path


def main():
    args = parsing_args()
    action = args.a
    name = args.n
    text = args.t
    func = funcs[action]
    if text:
        func(name, text)
    else:
        func(name)


class Git:
    def __init__(self):
        global action, name
        try:
            with open("active.txt") as f:
                self.active_project = f.readlines()
                self.active_name = self.active_project[0].split("-")[0].strip()
                self.active_path = self.active_project[0].split("-")[1].strip()

        except FileNotFoundError:
            if not action:
                sys.exit("there is no active projects, activate it via actp")
            self.actp(name)

    def crp(self, name, path):  # works
        with open("projects.txt", "a") as f:
            f.write(f"{name}-{path}\n")
        os.mkdir(f"{path}/commits")

    def crf(self, name):  # works
        x = open(f"{self.active_path}\{name}", "a")
        x.close()
        c = open(f"{self.active_path}\commits\{name}.txt", "w")
        c.close()

    def actp(self, name):  # works
        with open("projects.txt") as f:
            while 1:
                if name in (project := f.readline()):
                    break
        path = project.split("-")[1]
        with open("active.txt", "w") as f:
            f.write(f"{name}-{path}")

    def lc(self, name):  # works
        coms = []
        with open(f"{self.active_path}/commits/{name}.txt") as f:
            if m := re.findall(
                "---- START pygit COMMIT ----\n([\w\S].+)", "".join(f.readlines())
            ):
                for i, obj in enumerate(m):
                    print(i, obj)

    def scid(self, name, text):  # works
        with open(f"{self.active_path}/commits/{name}.txt") as f:
            if m := re.findall(
                "---- START pygit COMMIT ----\n([\w\S].+)", "".join(f.readlines())
            ):
                for i, obj in enumerate(m):
                    if text in obj:
                        print(i, obj)

    def retc(self, file, idc):
        with open(f"{self.active_path}\commits\{file}.txt") as f:
            code = "".join(f.readlines())
        new_code = re.findall(
            r"---- START pygit COMMIT ----\n[\w\S].*\n\n([\n\w\W\s\S]{1,}?)\n\n---- END pygit COMMIT ----",
            code,
        )
        with open(f"{self.active_path}/{file}", "w") as f:
            f.write(new_code[int(idc)])

    def addc(self, file, text):  # works
        with open(f"{self.active_path}/{file}") as f:
            code = f.readlines()
        with open(f"{self.active_path}/commits/{file}.txt", "a") as f:
            f.write("---- START pygit COMMIT ----\n")
            f.write(f"{text}\n\n")
            f.writelines(code)
            f.write("\n\n---- END pygit COMMIT ----\n\n\n\n")

    """def delc(self, id):
        ..."""  # why do I need this?

    def delf(self, name):  # works
        # ch = input('are you sure?')
        os.remove(f"{self.active_path}/{name}")
        os.remove(f"{self.active_path}/commits/{name}.txt")  # os.remove

    def delp(self, name):  # works
        with open("projects.txt") as f:
            li = f.readlines()
        for i in li:
            if re.search(rf"^{name}-\w", i):
                li.remove(i)
        with open("projects.txt", "w") as f:
            f.writelines(li)


cls = Git()

funcs = {
    "crp": cls.crp,
    "crf": cls.crf,
    "actp": cls.actp,
    "addc": cls.addc,
    "lc": cls.lc,
    "scid": cls.scid,
    "retc": cls.retc,
    "delf": cls.delf,
    "delp": cls.delp,
    # "delc": cls.delc,
}

if __name__ == "__main__":
    main()
