lst = []
with open('input.txt', 'r', encoding='utf-8-sig') as file:
    for i in range(8):
        f = file.readline().split()
        for line in f:
            lst.append(list(line))


def rook_hit(x, y):
    for i in range(x + 1, len(lst)):
        if lst[i][y] == 'R' or lst[i][y] == 'B':
            break
        lst[i][y] = 'h'
    for i in range(x - 1, -1, -1):
        if lst[i][y] == 'R' or lst[i][y] == 'B':
            break
        lst[i][y] = 'h'
    for j in range(y + 1, len(lst)):
        if lst[x][j] == 'R' or lst[x][j] == 'B':
            break
        lst[x][j] = 'h'
    for j in range(y - 1, -1, -1):
        if lst[x][j] == 'R' or lst[x][j] == 'B':
            break
        lst[x][j] = 'h'


def elephant_hit(x, y):
    break_flag = False
    k = x + y
    m = x - y
    for i in range(x + 1, len(lst)):
        for j in range(y + 1, len(lst)):
            if i - j == m:
                if lst[i][j] == 'R' or lst[i][j] == 'B':
                    break_flag = True
                    break
                lst[i][j] = 'h'
        if break_flag:
            break

    break_flag = False
    for i in range(x - 1, -1, -1):
        for j in range(y - 1, -1, -1):
            if i - j == m:
                if lst[i][j] == 'R' or lst[i][j] == 'B':
                    break_flag = True
                    break
                lst[i][j] = 'h'
        if break_flag:
            break

    break_flag = False
    for i in range(x + 1, len(lst)):
        for j in range(y - 1, -1, -1):
            if i + j == k:
                if lst[i][j] == 'R' or lst[i][j] == 'B':
                    break_flag = True
                    break
                lst[i][j] = 'h'
        if break_flag:
            break

    break_flag = False
    for i in range(x - 1, -1, -1):
        for j in range(y + 1, len(lst)):
            if i + j == k:
                if lst[i][j] == 'R' or lst[i][j] == 'B':
                    break_flag = True
                    break
                lst[i][j] = 'h'
        if break_flag:
            break


count_figures = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][j] == 'R':
            rook_hit(i, j)
            count_figures += 1
        if lst[i][j] == 'B':
            elephant_hit(i, j)
            count_figures += 1
for i in lst:
    print(i)
counter = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][j] == '*' or lst[i][j] == 'R' or lst[i][j] == 'B':
            counter += 1
print(counter - count_figures)

# lst = []
# lst = [['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '', '*', '*', '*', '*', '*'],
# ['*', '*', '*', 'B', '*', '*', '*', '*'],
# ['*', '*', 'R', '*', 'R', '*', '*', '*'],
# ['*', '*', 'B', '*', '*', '*', '*', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*']]
