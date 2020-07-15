import os
import os.path

a = []
for dir, subdir, files in os.walk('main'):

    for elem in files:
        if '.py' in elem and dir not in a:
            a.append(dir)
with open('find_py.txt', 'w') as o:
    for elem in sorted(a):
        o.writelines(elem + '\n')
