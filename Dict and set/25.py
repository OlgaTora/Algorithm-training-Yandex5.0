lst = []
for i in range(3):
    m = int(input())
    lst.append(set(map(int, input().split())))


def find2in3(lst):
    res = set()
    res = lst[0] & lst[1] | lst[0] & lst[2] | lst[1] & lst[2]
    print(' '.join(str(item) for item in sorted(res)))


find2in3(lst)
# find2in3([{3, 1}, {1, 3}, {1, 2}])
# find2in3([{1, 2, 2}, {3, 4, 3}, {5}])
