from cloudmesh.common.Shell import Shell


class sh:
    def list(self):
        L = Shell.execute('ls')
        print(L)

if __name__ == '__main__':
    list = sh()
    list.list()