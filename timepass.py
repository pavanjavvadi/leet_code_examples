a = [0,2,3]
b = [2, 6, 0, 4]
c = []

for i in a:
    if i in b:
        x = b.index(i)
        c.append(b[x + 1])
    else:
        c.append(i)

print(c)
