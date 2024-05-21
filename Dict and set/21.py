lst = []
n = int(input())
for i in range(n):
    m = int(input())
    lst.append(input().split(' '))


def best_playlist(n, lst):
    dct = {}
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            dct[lst[i][j]] = dct.get(lst[i][j], 0) + 1
    res = []
    for key, value in dct.items():
        if value == n:
            res.append(key)
    length = len(res)
    print(length)
    if length > 1:
        res.sort()
    for j in res:
        print(j, end=' ')


best_playlist(n, lst)
# best_playlist(2, [['Love', 'Life'], ['Life', 'GoodDay']])
# best_playlist(1, [['GoGetIt', 'Life']])
# best_playlist(2, [['m', 'b', 'j', 'y', 'a', 'l'], ['v', 'g', 'i', 'y', 'z', 'm', 'p', 'x', 'j']])
