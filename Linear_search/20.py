m, n = map(int, input().split())
lst = [input() for _ in range(m)]


def find_rectangles(m, n, lst):
    if n == 1 and m == 1: return print('NO')
    symb1 = '#'
    counter = [elem.count(symb1) for elem in lst]
    if sum(counter) < 2: return print('NO')

    def get_rigth_down(x1, y1, symb, x1_1=None, x1_2=None, y1_1=None, y1_2=None):
        # поиск правого нижнего угла
        for i in range(x1, m):
            if lst[i][y1] == symb1:
                x_max = i
            elif lst[i][y1] == 'a' and symb == 'b' and i in range(x1_1, x1_2 + 1) and i != m - 1:
                x_max = i
            else:
                break
        for j in range(y1, n):
            if lst[x1][j] == symb1:
                y_max = j
            elif lst[x1][j] == 'a' and symb == 'b' and j in range(y1_1, y1_2 + 1) and j != n - 1:
                y_max = j
            else:
                break
        for i in range(x1, x_max + 1):
            for j in range(y1, y_max + 1):
                if lst[i][j] == '.' and j <= y_max:
                    x_max = i - 1
        return x_max, y_max

    def check_rectangle(x1, y1, x2, y2, symb2):
        # закраска
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if lst[i][j] == '.':
                    break
                else:
                    lst[i] = lst[i][:j] + symb2 + lst[i][j + 1:]
        return lst

    def get_rectangle(lst, symb):
        x1, y1 = 0, 0
        flag = True
        while flag:
            for i in range(m):
                for j in range(n):
                    if lst[i][j] == symb1:
                        x1, y1 = i, j
                        x2, y2 = get_rigth_down(x1, y1, symb)
                        lst = check_rectangle(x1, y1, x2, y2, symb)
                        flag = False
                        return lst, x1, y1, x2, y2
                if flag == False: break

    def get_second_rectangle(lst, symb, x1_1, x1_2, y1_1, y1_2):
        # поиск второго прямоугольника
        x1, y1 = 0, 0
        flag = True
        while flag:
            for i in range(m):
                for j in range(n):
                    if lst[i][j] == symb1:
                        x1, y1 = i, j
                        x2, y2 = get_rigth_down(x1, y1, symb, x1_1, x1_2, y1_1, y1_2)
                        lst = check_rectangle(x1, y1, x2, y2, symb)
                        flag = False
                        return lst
                if flag == False: break

    lst, x1, y1, x2, y2 = get_rectangle(lst, symb='a')
    if not any(symb1 in elem for elem in lst):  # тут проверить можно ли разделить первый!!!
        if x1 == x2 and y1 == y2:
            return print('NO')
        elif x1 == x2:
            y2 = y1
            lst = check_rectangle(x1, y1, x2, y2, 'b')
        else:
            x2 = x1
            lst = check_rectangle(x1, y1, x2, y2, 'b')
    else:
        lst = get_second_rectangle(lst, 'b', x1, x2, y1, y2)

    if any(symb1 in elem for elem in lst): return print('NO')  # проверка остались ли #

    print('YES')
    return print("\n".join(item for item in lst))


find_rectangles(m, n, lst)

# find_rectangles(2, 1, ['#', '.']) #no
# find_rectangles(4, 4, ['....', '##..', '###.', '.##.']) #no
# find_rectangles(2, 4, ['.#..', '###.']) #23
# find_rectangles(5, 5, ['.....', '.###.', '.###.', '.###.', '.###.']) #15 YES ..... \ .abb. \ .abb. \ .abb. \ .abb.
# find_rectangles(3, 4, ['....', '..#.', '.##.']) #20 YES .... \ ..b. \ .ab.
# find_rectangles(4, 2, ['.#', '##', '.#', '..']) #24 YES ..... \ .abb. \ .abb. \ .abb. \ .abb.
# find_rectangles(4,  4, ['....', '###.', '###.', '###.']) # 11YES .... \ abb. \ abb. \ abb.
# find_rectangles(4,  2, ['..', '##', '##', '##']) #10YES .. \ ab \ ab \ ab
# find_rectangles(2, 2, ['.#', '.#']) #5
# find_rectangles(1, 3, ['###']) #5
# find_rectangles(3, 4, ['....', '.##.', '.#..'])
# find_rectangles(3, 4, ['....', '..#.', '.##.'])
# find_rectangles(3, 4, ['....', '.##.', '.#..'])
# find_rectangles(2, 5, ['#####', '##.##'])#, '#####', '#####', '#####']) #no
# find_rectangles(3, 5, ['.####', '.####', '.....'])
# find_rectangles(4, 5, ['.....', '..##.', '.##..', '.....'])
# find_rectangles(2, 3, ['...', '#.#'])
