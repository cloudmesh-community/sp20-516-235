import os
from cloudmesh.common.util import banner


class Provider:

    def list(self):
        banner("list")
        # os.system("multipass find")

    def shell(self):
        print("shell")
        # os.system("multipass shell")

    def run(self, command):
        print(f"run {command}")
        # os.system(f"multipass exec {command}")


if __name__ == "__main__":
    p = Provider()
    p.run("hallo")
    p.list()