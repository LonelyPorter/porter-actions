#!/usr/bin/python3

import tomllib as tb

class Project:
    def __init__(self, name:str, version: str):
        self.name = name

        self.major = version.split('.')[0]
        self.minor = version.split('.')[1]
        self.patch = version.split('.')[2]

    def __gt__(self, other):
        if self.major > other.major:
            return True
        elif self.major < other.major:
            return False

        if self.minor > other.minor:
            return True
        elif self.minor < other.minor:
            return False

        return self.patch > other.patch

    def __lt__(self, other):
        if self.major < other.major:
            return True
        elif self.major > other.major:
            return False

        if self.minor < other.minor:
            return True
        elif self.minor > other.minor:
            return False

        return self.patch < other.patch

if __name__ == "__main__":
    with open('project.toml', mode='rb') as fp:
        project = tb.load(fp)
        
        name = project['Project']['name']
        version = project['Project']['version']

        p = Project(name, version)