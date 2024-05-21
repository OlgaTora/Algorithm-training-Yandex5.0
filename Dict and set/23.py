n = int(input())
lst = list(map(int, input().split()))


def get_min4delete(n, lst):
    res, tmp = 0, 0
    if n == 1: return res
    dct = {}
    set_lst = list(set(lst))
    set_lst.sort()
    for i in range(n):
        dct[lst[i]] = dct.get(lst[i], 0) + 1

    res_lst = []
    for i in range(len(set_lst) - 1):
        if abs(set_lst[i] - set_lst[i + 1]) == 1:
            diff = dct.get(set_lst[i + 1], 0) + dct.get(set_lst[i], 0)
            res_lst.append(n - diff)
        else:
            tmp += 1
    res = tmp if tmp + 1 == len(set_lst) else min(res_lst)
    return res


print(get_min4delete(n, lst))
# print(get_min4delete(1, [33292])) #0
# print(get_min4delete(2, [1, 2]))
# print(get_min4delete(5, [1, 2, 3, 4, 5])) #3
# print(get_min4delete(10, [1, 1, 2, 3, 5, 5, 2, 2, 1, 5]))#4
