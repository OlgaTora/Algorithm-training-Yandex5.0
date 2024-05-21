n, k  =  map(int, input().split())
lst = list(map(int, input().split()))

def count_repeats(k, lst):
    if len(lst) == 1: return 'NO'

    dct = {}
    for i in lst:
        dct[i] = dct.get(i, 0) + 1

    dct_res = {}
    for key, value in dct.items():
        if value > 1:
            dct_res[key] = lst.index(key)
    # print(dct_res)

    flag = False
    for key, value in dct_res.items():
        for i in range(len(lst)):
            if lst[i] == key:
                if 0 < i - dct_res[key] <= k:
                    flag = True
                    break
                else:
                    dct_res[key] = i
        if flag == True: break
    return 'YES' if flag == True else 'NO'


print(count_repeats(k, lst))
# print(count_repeats(1, [1]))
# print(count_repeats(2, [1, 2, 3, 1]))
# print(count_repeats(1, [1, 0, 1, 1]))
# print(count_repeats(2, [1, 2, 3, 1, 2, 3]))
