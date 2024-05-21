n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]


def count_steps(n, lst):
    if n == 1: return 0
    y_coords = [i[1] for i in lst]
    if len(set(y_coords)) == 1: return 0
    steps = []
    lst.sort()
    for j in range(1, n):
        x_coords = [i[0] for i in lst if i[1] == j]
        step = 0
        for i in range(n):
            if lst[i][1] != j:
                if lst[i][0] not in x_coords:
                    step += abs(lst[i][1] - j)
                    x_coords.append(lst[i][0])
                else:
                    for k in range(1, n + 1):
                        if k not in x_coords:
                            step += (abs(lst[i][1] - j) + abs(lst[i][0] - k))
                            x_coords.append(k)
                            break
        steps.append(step)
    print(steps)
    return min(steps)


print(count_steps(n, lst))
# print(count_steps(4, [[1,1], [2,1], [3,2], [1,4]])) #7
# print(count_steps(3, [[1,2], [3,3], [1,1]])) #t1 3
# print(count_steps(1, [[1,1]])) #0
# print(count_steps(2, [[1,1], [2,2]])) #1
# print(count_steps(2, [[1,1], [2,1]])) #0
# print(count_steps(2, [[1,1], [1,2]])) #2
# print(count_steps(3, [[1, 1],[2, 1],[3, 1]])) #0
# print(count_steps(5, [[1, 5], [2, 4],[3, 3],[4, 2],[5, 1]])) #t10 6
# print(count_steps(10, [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6],
#                        [7, 7], [8, 8], [9, 9], [10, 10]])) #t11 25
# print(count_steps(10, [[1, 6], [6, 2], [5, 5], [7, 5], [8, 9], [6, 10],
#                        [8, 2], [10, 8], [8, 7], [7, 8]])) #t17 37
# print(count_steps(10, [[9, 4], [8, 9], [5, 4], [10, 8], [7, 9], [10, 5],
#                        [9, 2], [8, 10], [3, 9], [6, 2]]))#t13 48
