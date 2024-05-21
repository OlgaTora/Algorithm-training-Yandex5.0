n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]


def search_two_max(n, m, lst):
    max_n = 0
    for i in range(len(lst)):
        if max_n < max(lst[i]):
            max_n = max(lst[i])
            idx_i = i
            idx_j = lst[i].index(max_n)
    print(f'i= {idx_i} j={idx_j} max={max_n}')

    def search_max_without(idx_i, idx_j):
        max_m_row, max_m_col = 0, 0
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] > max_m_row and i != idx_i:
                    max_m_row = lst[i][j]
                    max_m_ir = i
                    max_m_jr = j
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] > max_m_col and j != idx_j:
                    max_m_col = lst[i][j]
                    max_m_ic = i
                    max_m_jc = j
        print(f'i= {max_m_ir} j={max_m_jr} max={max_m_row}')
        print(f'i= {max_m_ic} j={max_m_jc} max={max_m_col}')
        return max_m_row, max_m_jr, max_m_col, max_m_ic

    def search_last_max(idx_i, idx_j):
        max_m = 0
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] > max_m and i != idx_i and j != idx_j:
                    max_m = lst[i][j]
                    max_m_i = i
                    max_m_j = j
        print(f'i= {max_m_i} j={max_m_j} max={max_m}')
        return max_m, max_m_i, max_m_j

    max_m_row, max_m_jr, max_m_col, max_m_ic = search_max_without(idx_i, idx_j)
    max_m1, max_m_i1, max_m_j1 = search_last_max(max_m_ic, idx_j)
    max_m2, max_m_i2, max_m_j2 = search_last_max(idx_i, max_m_jr)

    print(f'{idx_i + 1} {max_m_jr + 1}') if max_m1 > max_m2 else \
        print(f'{max_m_ic + 1} {idx_j + 1}')


search_two_max(n, m, lst)
# search_two_max(2, 2, [[1, 2], [3, 4]]) # 2 2
# search_two_max(3, 4,  [[1,3,5,7], [9,11,2,4], [6,8,10,12]]) # 3 2
# search_two_max(6, 6, [[1, 2, 3, 4, 5, 6],\
#                        [100, 2, 4, 100, 1, 100],\
#                        [2, 3, 4, 5, 1, 2],\
#                        [5, 3, 5, 3, 5, 3],\
#                        [1, 2, 1, 2, 1, 2],\
#                        [3, 3, 3, 3, 3, 3]])
# search_two_max(4, 5, [[999999997, 1, 2, 3, 4], [10, 2, 1000000000, 1, 7],\
#                       [3, 9, 999999999, 5, 10], [1, 7, 3, 999999998, 6]])
