coords = [list(map(int, input().split())) for _ in range(int(input()))]


def get_square(coords):
    if len(coords) == 1:
        x = coords[0][0]
        y = coords[0][1]
        res = {3: [[x + 1, y], [x, y + 1], [x + 1, y + 1]]}
    elif len(coords) == 2:
        res = {2: [[coords[0][0], coords[1][1]], [coords[1][0], coords[0][1]]]}
    else:
        dct = {}
        for coord in coords:
            dct.setdefault(coord[0], []).append(coord[1])
        flag = True
        res = {}
        for c1 in range(len(coords)):
            if flag == False: break
            for c2 in range(c1 + 1, len(coords)):
                x1, y1 = coords[c1][0], coords[c1][1]
                x2, y2 = coords[c2][0], coords[c2][1]
                d = ((x2 - x1) - (y1 - y2)) / 2
                x3, y3 = x1 + d, y2 - d
                x4, y4 = x2 - d, y1 + d
                if y3 in dct.get(x3, []) and y4 in dct.get(x4, []):
                    flag = False
                    return print('0')
                elif y3 in dct.get(x3, []):
                    res[1] = res.get(1, [[x4, y4]])
                elif y4 in dct.get(x4, []):
                    res[1] = res.get(1, [[x3, y3]])
                else:
                    if int(x3) == x3 and int(x4) == x4 and int(y3) == y3 and int(y4) == y4:
                        res[2] = res.get(1, [[x3, y3], [x4, y4]])
                if flag == False: break

    def print_func(res):
        res = list(map(lambda n: list(map(int, n)), res.get(min(res.keys()))))
        print(len(res))
        for i in res:
            print(*i, end='\n')

    return print_func(res)


get_square(coords)

# get_square([[0,0]])
# get_square([[0,1], [1,0]])
# get_square([[-9, 6], [7, -2], [-5, -6]])
# get_square([[-1, 1], [1, 1], [-1, -1], [1, -1]])
# get_square([[0, 2], [2, 0], [2, 2]])
# get_square([[-1, 1], [1, 1], [-1, -1], [1, -1]])
# get_square([[8, 6], [-9, 6], [-4, 1], [-5, 3], [6, 4], [7, -2], [9, 2],\
#              [9, 8], [8, 10], [-7, -2], [-5, -6], [1, 7]])
# get_square([[-3, 3], [5, 4], [-9, -1], [0, 4], [7, -2], [1, 8],\
# [3, 4], [8, -1], [-1, -2], [10, 6], [-2, -8], [-6, -6], [5, -10], [1, 5],\
# [-4, -4], [-9, 6], [-9, -7], [0, 7], [3, -7], [-4, 1], [1, 0]])
# get_square([[-61366792, -62843276], [-40815926, 19011845],\
# [28942849, -88271603], [52193328, -77715111], [38336116, -14051365],\
# [-34724931, -61880077], [-42603797, 57331589], [30617711, 32266737],\
# [49957576, -2084616]])
