def func(v1, v2):
    return v1 + v2


def func2(args):
    return args ** 2


x = func2(func(1, 2))

print(x)
