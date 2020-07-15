from xml.etree import ElementTree
#inp = '<cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>'

def whos_child(par, index):
    index += 1
    val[par.attrib['color']] += index
    for child in list(par):
        whos_child(child, index)


root = ElementTree.fromstring(input())
val = {'red': 0, 'green': 0, 'blue': 0}
index = 1
val[root.attrib['color']] = index
for child in list(root):
    whos_child(child, index)
print(*val.values())