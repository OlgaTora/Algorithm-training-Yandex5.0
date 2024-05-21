lst = [list(map(int, input().split())) for _ in range(int(input()))]


def get_optimum_berries(lst):
    global tmp_after, tmp_before
    res_after, res_before, max_res, res = 0, 0, 0, 0
    min_after_zero, max_before_zero = 0, 0
    indexes_after = []
    indexes_before = []
    for i in range(len(lst)):
        if lst[i][0] - lst[i][1] >= 0:
            indexes_after.append(i + 1)
            res = res + lst[i][0] - lst[i][1]
            if min_after_zero < lst[i][1]:
                min_after_zero = lst[i][1]
                tmp_after = i + 1
        else:
            indexes_before.append(i + 1)
            if max_before_zero < lst[i][0]:
                max_before_zero = lst[i][0]
                tmp_before = i + 1

    res_after = res + min_after_zero
    res_before = res + max_before_zero if res != 0 else max_before_zero
    max_res = max(res_after, res_before)
    print(max_res)
    # tmp_after, tmp_before = 0, 0
    if min_after_zero != 0:
        indexes_after.remove(tmp_after)
        indexes_after.append(tmp_after)
    if max_before_zero != 0:
        indexes_before.remove(tmp_before)
        indexes_after.append(tmp_before)

    indexes_after += indexes_before
    for i in indexes_after:
        print(i, end=' ')


get_optimum_berries(lst)
# get_optimum_berries([[7, 4], [7, 6], [6, 5]]) # 11
# get_optimum_berries([[6, 2], [3, 1], [8, 5]]) # 14
# get_optimum_berries([[1, 5], [8, 2], [4, 4]]) # 10 2 3 1
# get_optimum_berries([[7, 6], [7, 4]]) # 10 2 1
# get_optimum_berries([[7, 3]]) # 7
