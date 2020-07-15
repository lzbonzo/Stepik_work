def create(name,parent = 'global'):
    namespace[name] = [parent]

def add(name,var):
    namespace[name].append(var)

def get(name, var):
    if name is None:
        print(None)
    else:
        if var in namespace.get(name) and name is not None:
            print(name)
        else:
            return get(namespace.get(name)[0], var)

a = 0
n = int(input())
namespace = {'global': [None]}
for i in range(n):
    cmd, name, arg = input().split()
    if cmd == 'create':
        create(name,arg)
    elif cmd == 'add':
        add(name,arg)
    elif cmd == 'get':
        get(name, arg)