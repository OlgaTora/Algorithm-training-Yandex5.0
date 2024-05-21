V, M = [input().split() for i in range(2)]
p, v = int(V[0]), int(V[1])
q, m = int(M[0]), int(M[1])

if (m + q < p - v) or (p + v < q - m):
    res = (v * 2 + 1) + (m * 2 + 1)
else:
    lst = [q - m, m + q, p - v, p + v]
    lst = sorted(lst)
    res = abs(min(lst)) + max(lst) + 1
print(res)
