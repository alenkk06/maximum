spisok=(x**2 for x in range(1000000))
print(spisok)

def gen():
    for x in range(1000000):
        yield x**2
for x in gen():
    print(x)
