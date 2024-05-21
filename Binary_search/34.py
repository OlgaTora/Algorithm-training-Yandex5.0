words1, words2 = [], []
with open('34(16)', 'r') as file:
    w, n, m = map(int, file.readline().split())
    f = map(int, file.readline().split())
    for line in f:
        words1.append(line)
    f = map(int, file.readline().split())
    for line in f:
        words2.append(line)


def check(part):
    rows1 = rows_counter(part, words1)
    rows2 = rows_counter(w - part, words2)
    return rows1, rows2


def binary_search():
    min_part1 = max(words1)
    min_part2 = max(words2)
    l, r = min_part1, w - min_part2
    result = []
    num = l + (r - l) // 2
    while l <= r:
        rows1, rows2 = check(num)
        result.append((max(rows1, rows2)))
        if l == r:
            break
        if rows1 < rows2:
            r = num
        elif rows1 > rows2:
            l = num + 1
        else:
            return min(result)
        num = (r + l) // 2
    return min(result)


def rows_counter(part: int, words: list) -> int:
    count_rows = 0
    complete_row = 0
    for i in range(len(words)):
        elem = complete_row + words[i]
        if elem == part or elem + 1 == part:
            count_rows += 1
            complete_row = 0
        elif elem + 1 < part:
            complete_row += words[i] + 1
        elif elem + 1 > part:
            count_rows += 1
            complete_row = words[i] + 1
    if complete_row != 0:
        count_rows += 1
    return count_rows


print(binary_search())
# w = 10 #res 4
# words1 = [1, 1, 2, 1, 2]
# words2 = [7, 7, 1, 5, 5]
# w = 10 #res 9
# words1 = [4, 1, 2, 2, 3, 2, 5, 2, 2, 1]
# words2 = [4, 1, 4, 1, 5, 5, 1, 2, 2, 3]
# w, n, m = 10, 5, 5
# words1 = [1, 1, 1, 1, 1]
# words2 = [5, 2, 3, 3, 4]
# w, n, m = 10, 10, 1
# words1 = [1, 1, 1, 1, 1, 1,1,1,1,1]
# words2 = [438]