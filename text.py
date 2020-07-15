a = []
with open('input.txt') as f:
    for line in f:
        a.append(line.rstrip())
with open('output.txt', 'w') as o:
    for i in reversed(range(len(a))):
        o.write(a[i] + '\n')