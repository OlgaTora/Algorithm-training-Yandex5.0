l, x1, v1, x2, v2 = map(int, input().split())

def search_t(l, x1, v1, x2, v2):
    t = 0
    if v1 == 0 and v2 == 0:
        t = 'NO' if x1 != x2 else 0
    elif x1 == x2:
        t = 0
    elif v1 == 0:
        t = (l - x2 - x1) / v2 if x2 > x1 else (l - x1 - x2) / v2
    elif v2 == 0:
        print(f'v2  x1={x1} x2={x2}')
        t = (l - x1 - x2) / v1 if x1 > x2 else (x2 - x1) / v1
    elif abs(v1) == abs(v2):  # x1 != x2
        t1 = ((l - abs(x2 - x1)) / 2 - x2) / v1 if x1 > x2 else ((l - abs(x1 - x2)) / 2 - x1) / v2
        t2 = (x1 + (abs(x1 - x2)) / 2) / v2
        t = min(t1, t2)
        if v1 == -v2:
            t = (l + x2 - x1) / (v1 - v2)
    else:  # x1 != x2
        if x1 > x2 and abs(v1) < abs(v2):
            t1 = (x2 - x1) / (v1 - v2)
            t2 = (x1 + x2) / (v1 + v2)
            t = min(abs(t1), abs(t2))
        else:
            t1 = (2 * l - x1 - x2) / (v1 + v2)
            t2 = (l + x1 - x2) / (abs(v2) + abs(v1))
            t = min(abs(t1), abs(t2))
    return t


t  = search_t(l, x1,v1,x2,v2)
print(t) if type(t) == str else print(f'YES\n{abs(t)}')
#
# print(search_t(6, 3, 1, 1, 1))  # 1
# print(search_t(6, 1, 1, 4, 1))  # 0.5
# print(search_t(12, 8, 10, 5, 20))  # 0.3
# print(search_t(762899414, 556082848, -539099316, 556082848, -582799403))  # 0
# print(search_t(5, 0, 0, 1, 2))  # 2
# print(search_t(10, 7, -3, 1, 4))  # 0.8517
# print(search_t(948744004, 861724643, 848773505, 584154450, 730556189))  # 0.285949
# print(search_t(72036282, 55132452, -373561948, 11464466, -887525183))  # 0.0528091330 !!!
# print(search_t(615143346, 79387687, -80123649, 306422480, -80123649))  # 2.407529
# print(search_t(94, 76, 0, 76, 0))  # 0
# print(search_t(977345779, 636176199, 0, 165786447, 815181433))  # 0.215146
# print(search_t(72, 20, -38121735, 66, 288888467))  # 0.0000000795
# print(search_t(59444, 48811, 596232464, 1681, 596232464))  # 0.0000075071
# print(search_t(55444931, 17419156, 0, 53245822, -398046024))  # 0.0382369025
# print(search_t(1000000000, 10, 1000000000, 11, 0))  # 0.0000000010
# print(search_t(1000000000, 1, 1, 0, 0))
# ##print(search_t(12, 5,1, 8,2))
# print(search_t(78118007, 46215547, -5, 57496922, 9))  # 4774045.1428571429
# print(search_t(956390104, 549514100, 7, 315097830, -7))  # 51569559.5714285714
# print(search_t(1, 0, 0, 0, 0))  # 0
