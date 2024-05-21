with open('26', 'r', encoding='utf-8-sig') as file:
    lst_dict = file.readline().split()
    lst = file.readline().split()


def cut2dict(lst_dict, lst):
    dct = {}
    lst_dict.sort()
    for i in lst_dict:
        tmp = tuple(dct.get(i[:1], ()))
        if not i.startswith(tmp):
            dct.setdefault(i[:1], set()).add(i)
    res = []
    for j in lst:
        if j[:1] not in dct.keys():
            res.append(j)
        else:
            for k in dct[j[:1]]:
                if j.startswith(k):
                    res.append(k)
                    break
            else:
                res.append(j)
    for i in res:
        print(i, end=' ')


cut2dict(lst_dict, lst)
# cut2dict(['a', 'b'], ['abdafb', 'basrt', 'casds', 'dsasa', 'a']) #a b casds dsasa a
# cut2dict(['aa', 'bc', 'aaa'], ['a', 'aa', 'aaa', 'bcd', 'abcd']) #  a aa aa bc abcd
