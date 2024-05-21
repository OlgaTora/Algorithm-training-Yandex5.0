n = int(input())
lst = list(map(int, input().split()))


def search_symb(lst):
    res = ''
    if len(lst) == 2:
        res = chr(43) if lst[0] % 2 == 0 else chr(120)
    elif len([i for i in lst if i % 2 != 0]) % 2 != 0:
        res += chr(43) * (n - 1)
    else:
        for i in range(1, len(lst)):
            if lst[i] % 2 == 0:
                res += chr(43)
            else:
                res += chr(120)
                res += chr(43) * (n - len(res) - 1)
                break
    return res


print(search_symb(lst))
