objects = [1, 2, [3, 2], 1]


ans = set()
for obj in objects:
    ans.add(id(obj))

print(len(ans))