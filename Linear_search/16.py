sectors = int(input())
lst = list(map(int, input().split()))
v0, v1, k = map(int, input().split())


def get_fortune(sectors, lst, v0, v1, k):
    max_prize = 0
    if v1 <= k: return lst[0]
    if k == 1 and v1 > sectors: return max(lst)
    if v1 - v0 >= k * sectors and v1 > sectors * k: return max(lst)
    for v in range(v0, v1 + 1, k):
        borders = v // k if v % k != 0 else v // k - 1
        diff = borders % sectors
        if diff == 0:
            max_prize = lst[0] if max_prize < lst[0] else max_prize
        elif borders < sectors:
            max_prize = lst[borders] if max_prize < lst[borders] else max_prize
            max_prize = lst[sectors - borders] if max_prize < lst[sectors - borders] else max_prize
        else:
            max_prize = lst[diff] if max_prize < lst[diff] else max_prize
            max_prize = lst[- diff] if max_prize < lst[- diff] else max_prize
    return max_prize


print(get_fortune(sectors, lst, v0, v1, k))
# print(get_fortune(5, [1,2,3,4,5], 3, 5, 2)) #5
# print(get_fortune(5, [1, 2, 3, 4, 5], 15, 15, 2)) #4
# print(get_fortune(5, [5, 4, 3, 2, 1], 2, 5, 2)) #5
# print(get_fortune(5, [692, 407, 437, 964, 10], 49, 79, 384)) #692
# print(get_fortune(9, [707,805, 279, 713, 584, 352, 923, 1000, 237],29, 38, 1)) #1000
# print(get_fortune(7, [499, 871, 917, 409, 203, 830, 482], 5, 34, 5)) #917
# print(get_fortune(4, [744, 43, 468, 382],20, 48, 12)) #468
