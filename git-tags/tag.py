import tomllib as tb
import subprocess as sp

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
    
    def __eq__(self, other):
        return self.major == other.major and \
            self.minor == other.minor and \
            self.patch == other.patch

if __name__ == "__main__":
    with open('project.toml', mode='rb') as fp:
        project = tb.load(fp)
        
        name = project['Project']['name']
        version = project['Project']['version']

        now_p = Project(name, version)
    
    output = sp.check_output(["git", "show", "HEAD^:project.toml"])
    
    project = tb.loads(output.decode())
    name = project['Project']['name']
    version = project['Project']['version']
    last_p = Project(name, version)
    
    print(now_p > last_p, now_p == last_p)