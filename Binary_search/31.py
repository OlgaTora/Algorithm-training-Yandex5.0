m = int(input())
lst = list(map(int, input().split()))
k = int(input())
requests = [list(map(int, input().split())) for _ in range(k)]


# lst = [1, 3, 4, 10, 10]
# requests = [[1, 10], [2, 9], [3, 4], [2, 2]] #5 2 2 0

def check_number_less(num, request):
    return True if request[0] <= lst[num] else False


def check_number_more(num, request):
    return True if request[-1] >= lst[num] else False


lst.sort()
res = []
for request in requests:
    l, r = -1, len(lst)
    while l + 1 < r:
        num = (l + r + 1) // 2
        if check_number_more(num, request):
            l = num
        else:
            r = num
    res1 = l
    l = -1
    while l + 1 < r:
        num = (l + r) // 2
        if check_number_less(num, request):
            r = num
        else:
            l = num
    res2 = l
    res.append(str(res1 - res2))

print(' '.join(res))
