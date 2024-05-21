word1, word2 = input(), input()


def annogramm(word1, word2):
    dct1, dct2 = {}, {}
    for letter in word1:
        dct1[letter] = dct1.get(letter, 0) + 1
    for letter in word2:
        dct2[letter] = dct2.get(letter, 0) + 1
    print('YES') if dct1 == dct2 else print('NO')


annogramm(word1, word2)
# annogramm('dusty', 'study')
