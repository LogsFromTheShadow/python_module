def fun(max):
    count = 1
    while count <= max:
        yield count
        count += 1


iteration = fun(5)

for x in iteration:
    print(x)
