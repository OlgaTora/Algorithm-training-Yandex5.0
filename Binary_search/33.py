n, m = map(int, input().split())
orcs = list(map(int, input().split()))


def get_summ_from_num(num, quantity):
    if num - quantity >= 0:
        summ = prefix_sum[num] - prefix_sum[num - quantity]
    else:
        summ = prefix_sum[num]
    return summ


def binary_search(company):
    if company[0] > n:
        return -1
    l, r = company[0] - 1, len(orcs) - 1
    while l < r:
        num = (l + r) // 2
        condition = get_summ_from_num(num, company[0])
        if condition == company[1]:
            return (num - company[0] + 1) + 1
        elif condition > company[1]:
            r = num
        else:
            l = num + 1
    if get_summ_from_num(l, company[0]) == company[1]:
        return (l - company[0] + 1) + 1


prefix_sum = [0] * len(orcs)
prefix_sum[0] = orcs[0]
for j in range(1, len(orcs)):
    prefix_sum[j] = prefix_sum[j - 1] + orcs[j]

for i in range(m):
    company = list(map(int, input().split()))
    res = binary_search(company)
    print(res) if res is not None else print(-1)

# 5, 2, [1, 3, 5, 7, 9], [[2, 4]])#, [1, 3]] # 1 2
# 5, 10, [570703232, 570703232, 570703232, 570703232, 570703232],\
# [[2, 687772523], [1, 570703232], [1, 570703232], [1, 570703232], [1, 570703232],\
# [1, 570703232], [2, 1141406464], [1, 570703232], [1, 570703232], [3, 1712109696]]
