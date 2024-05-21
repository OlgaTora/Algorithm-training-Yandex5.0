lst = [list(map(int, input().split())) for _ in range(int(input()))]


def get_perimeter(lst):
    summ = len(lst) * 4
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][0] == lst[j][0] and lst[j][1] - lst[i][1] == 1:
                summ -= 2
            if lst[i][1] == lst[j][1] and lst[j][0] - lst[i][0] == 1:
                summ -= 2
    return summ


print(get_perimeter(lst))

# print(get_perimeter([[1, 1], [1, 2], [2, 1]]))
# print(get_perimeter([[8, 8]]))
# print(get_perimeter([[3, 4], [3, 5], [3, 6], [3, 7]]))
