n = int(input())
#собрал словарь
exc = {}
for _ in range(n):
    a = input().split()
    exc[a[0]] = [] if len(a) == 1 else a[2:]

#является предком
def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), exc[child]))

#список исключений
exlist = []
m = int(input())
for _ in range(m):
    exlist.append(input())
#print(exlist)
errorlist = []
for elem in exlist:
    for i in range(exlist.index(elem) + 1, m):
        if is_parent(exlist[i], elem) and exlist[i] not in errorlist:
            errorlist.append(exlist[i])
sortdict = {}
for elem in errorlist:
    sortdict[elem] = exlist.index(elem)
for i in range(m):
    for key, values in sortdict.items():
        if i == values:
            print(key)



