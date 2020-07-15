def depth(par,ch):
    if par not in all or ch not in all:
        return False
    if ch == par:
        return True

    if par in tree[ch]:
        return True

    return False

tree = {}
all = set()
for _ in range(int(input())):
    ch, *par = input().split(' : ')
    if par == []:
        tree[ch] = par
    else:
        tree[ch] = par[0].split()
    all.add(ch)
    for elem in tree[ch]:
        all.add(elem)

for k, v in tree.items():
    for k2, v2 in tree.items():
        if k in v2:
            v2 += v

for i in range(int(input())):
    par, ch = input().split()
    if depth(par, ch) is True:
        print('Yes')
    else:
        print('No')