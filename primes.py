def primes():
    i = 2
    while True:
        q = 0
        for j in range(2, i + 1):
            if i % j == 0:
                q += 1
        if q == 1:
             yield (i)
        i += 1



x = primes()
for elem in x:
    print(elem)