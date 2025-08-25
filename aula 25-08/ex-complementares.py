def func(int1, int2):
    if int2 == 0:
        return 0
    else:
        return int1 + func(int1, int2-1)

print(func(4,5))