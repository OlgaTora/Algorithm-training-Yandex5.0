n = int(input())
lst = list(map(int, input().split()))


def search_min_length(n, lst):
    max_length = max(lst)
    ind = lst.index(max_length)
    res = sum(lst[:ind] + lst[ind + 1:])
    if max_length - res > 0:
        print(max_length - res)
    else:
        print(res + max_length)


search_min_length(n, lst)
#
# search_min_length(4, [1, 5, 2, 1])  # 1
# search_min_length(4, [5, 12, 4, 3])  # 24
# search_min_length(2, [1000, 1000])  # 2000
# search_min_length(2, [999, 1000])  # 1
