import json

def inherit(par):
    while True:
        for k,v in class_tree.items():
            
            if par in v:
                inherit_tree[par].add(k)
                par = k
                inherit(par)


'''
Ответ:

A : 5
B : 1
C : 4
D : 2
E : 1
F : 3
'''


with open('class.json') as f:
    class_tree_json = json.load(f)

#class_tree_json = json.loads(input())

class_tree = {}
inherit_tree = {}
for elem in class_tree_json:
    class_tree[elem['name']] = elem['parents']
    inherit_tree[elem['name']] = set()
print(class_tree)
print(inherit_tree)
for elem in inherit_tree:
    inherit(elem)

for elem in sorted(inherit_tree):
    print(elem, inherit_tree[elem])

