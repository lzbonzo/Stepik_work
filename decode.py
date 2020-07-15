with open('dataset_3363_2.txt') as inf:
    s = inf.readline()
o = ''
for i in range(len(s)):
    c = ' '
    if s[i].isalpha():
        l = s[i]
        i += 1
        while s[i].isdigit():
            c += str(s[i])
            i += 1
            if s[i].isalpha():
                break
        o += l * int(c)
#print(o)
with open('output.txt', 'w') as ouf:
    ouf.write(o)
