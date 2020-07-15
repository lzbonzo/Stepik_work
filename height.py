#t = []

with open('dataset_3380_5.txt') as inf:
    t = inf.read().rstrip().split('\n')
        #t.append(inf.readlines())
o = {}
for elem in t:
    k, s, h = elem.split('\t')
    if k not in o:
        o[k] = [int(h), 1]
    else:
        o[k] = [o.get(k)[0] + int(h),o.get(k)[1] + 1]
for i in range(1,12):
    if str(i) not in o:
        o[i] = '-'
print(o)
with open('output.txt', 'w') as ouf:
    for i in range(1,12):
        q = str(i) + ' ' + str(int(o[str(i)][0])/int(o[str(i)][1])) + '\n'
        ouf.write(q)
