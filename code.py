def dec(w):
    o = ''
    for i in range(len(w)):
        o += dict[w[i]]
    print(o)


def decin(w):
    o = ''
    for i in range(len(w)):
        for key, val in dict.items():
            if val == w[i]:
                o += key
    print(o)


l = str(input())
code = str(input())
dict = {}
for i in range(len(l)):
    dict[l[i]] = code[i]
word = str(input())
c = str(input())
dec(word)
decin(c)
