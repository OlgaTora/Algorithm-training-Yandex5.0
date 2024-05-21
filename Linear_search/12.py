n, k = map(int, input().split())
lst = list(map(int, input().split()))


def get_profit(n, k, lst):
    res = 0
    if n == 0 or n == 1: return 0
    for i in range(0, n):
        for j in range(i, n):
            if j - i <= k:
                res = lst[j] - lst[i] if lst[j] - lst[i] > res else res
    return res


print(get_profit(n, k, lst))
# print(get_profit(5, 2, [1,2,3,4,5])) #2
# print(get_profit(5,2, [5,4,3,2,1])) #0
# print(get_profit(1,1, [1])) #0
# print(get_profit(10, 10, [6, 7, 5, 5, 10, 10, 1, 8, 5, 10])) #9
# print(get_profit(2,1, [1, 2])) #1
# print(get_profit(10, 7, [9, 4, 9, 3, 8, 10, 9, 4, 5, 5])) #7
