n, k, d = input().split()


def count_amount(n, k, d):
    figures = '1234567890'
    counter = 0
    for figure in figures:
        tmp = int(n + figure)
        if tmp % k == 0:
            n = str(tmp)
            break
        else:
            counter += 1
    if counter == len(figures):
        return -1
    n = n + '0' * (d - 1)
    return n


d = int(d)
k = int(k)
print(count_amount(n, k, d))
