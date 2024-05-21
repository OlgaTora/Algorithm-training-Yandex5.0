# NOT DONE

# n = int(input())
# coords1 = [list(map(int, input().split())) for _ in range(n)]
# coords2 = [list(map(int, input().split())) for _ in range(n)]
n = 8
coords1 = [[10000, 0, 7071, 7071], [7071, 7071, 0, 10000], [0, 10000, -7071, 7071], [-7071, 7071, -10000, 0],
           [-10000, 0, -7071, -7071], [-7071, -7071, 0, -10000], [0, -10000, 7071, -7071], [7071, -7071, 10000, 0]]
coords2 = [[7071, -7071, 10000, 0], [7070, -7070, 9999, 1], [7069, -7069, 9998, 2], [7068, -7068, 9997, 3],
            [7067, -7067, 9996, 4], [7066, -7066, 9995, 5], [7065, -7065, 9994, 6], [7064, -7064, 9993, 7]]

# n = 5
# coords1 = [[0, 0, 1, 2], [1, 0, 0, 2], [2, 0, 2, 2], [4, 0, 3, 2], [4, 0, 5, 2]]
# coords2 = [[9, -1, 10, 1], [10, 1, 9, 3], [8, 1, 10, 1], [8, 1, 9, -1], [8, 1, 9, 3]]
# n = 1
# coords1 = [[3, 4, 7, 9]]
# coords2 = [[-1, 3, 3, 8]]
# n = 1
# coords1 = [[-4, 5, 2, -3]]
# coords2 = [[-12, 4, -2, 4]]

# def count_matches():
def get_distance(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if n == 1:
    d1 = get_distance(coords1[0][0], coords1[0][2], coords2[0][0], coords2[0][2])
    d2 = get_distance(coords1[0][1], coords1[0][3], coords2[0][1], coords2[0][3])
    d3 = get_distance(coords1[0][0], coords1[0][2], coords2[0][1], coords2[0][3])
    d4 = get_distance(coords1[0][1], coords1[0][3], coords2[0][0], coords2[0][2])
    len1 = get_distance(coords1[0][0], coords1[0][2], coords1[0][1], coords1[0][3])
    len2 = get_distance(coords2[0][0], coords2[0][2], coords2[0][1], coords2[0][3])
    print('0') if len1 == len2 and (d1 == d2 or d3 == d4) else print('1')
else:
    res = []
    dct = {}
    for i in range(n):
        name_i = name = ''.join([str(_) for _ in coords1[i]])
        len1 = get_distance(coords1[i][0], coords1[i][2], coords1[i][1], coords1[i][3])
        for j in range(i + 1, n):
            name_j = name = ''.join([str(_) for _ in coords2[j]])
            len2 = get_distance(coords2[j][0], coords2[j][2], coords2[j][1], coords2[j][3])
            if len1 == len2:
                name = name_i + name_j
                dx1, dx2 = coords1[i][0] - coords2[j][0], coords1[i][2] - coords2[j][2]
                dy1, dy2 = coords1[i][1] - coords2[j][1], coords1[i][3] - coords2[j][3]
                if dx1 == dy1 or dx2 == dy2:
                    dct[name] = dct.get(name, set())#.get(d1, set
                else: break
                for k in range(j + 1, n):
                    name_k = ''.join([str(_) for _ in coords1[k]])
                    len3 = get_distance(coords1[k][0], coords1[k][2], coords1[k][1], coords1[k][3])
                    for m in range(k + 1, n):
                        name_m = ''.join([str(_) for _ in coords2[m]])
                        len4 = get_distance(coords2[m][0], coords2[m][2], coords2[m][1], coords2[m][3])
                        if len3 == len4:
                            dx3, dx4 = coords1[k][0] - coords2[m][0], coords1[k][2] - coords2[m][2]
                            dy3, dy4 = coords1[k][1] - coords2[m][1], coords1[k][3] - coords2[m][3]
                            # d8 = get_distance()
                            if dx3 == dy3 == dx1:
                                dct[name].add(name_k)
                                dct[name].add(name_m)
    for k, v in dct.items():
        print(k, v)

    # print(dct)
    #     matches = 0
    # for k, v in dct.items():
    # #         # matches += len(v)
    #     print(k, v)
    #     res.append(n - matches // 2)
    # print(min(res))
