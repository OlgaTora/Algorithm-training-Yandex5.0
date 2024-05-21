lst = [int(input()) for i in range(int(input()))]


def count_xyz(n):
    x, y, z = 0, 0, 0
    if n % 4 == 0:
        return n // 4
    else:
        y = n // 4
        n = n % 4
        if n == 1:
            x = 1
        elif n == 2:
            x = 2
        else:
            y += 1
            z = 1
        return x + y + z


res = [count_xyz(i) for i in lst]
print(sum(res))
