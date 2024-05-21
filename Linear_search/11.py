lst = [list(map(int, input().split())) for j in range(int(input()))]
# lst = [[1, 3], [3, 11], [3, 5], [6, 3]]
x_lst = [i[0] for i in lst]
y_lst = [i[1] for i in lst]
print(f'{min(x_lst)} {min(y_lst)} {max(x_lst)} {max(y_lst)}')