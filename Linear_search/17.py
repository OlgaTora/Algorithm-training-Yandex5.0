def search_min(numbers):
    if len(numbers) == 1:
        return f'1\n1'
    res = [1]
    length, min_num = 0, numbers[0]
    for num in range(1, len(numbers)):
        #   print(f'i= {num} num= {numbers[num]} len= {length}, res={res}')
        if numbers[num] > res[length]:
            if numbers[num] < min_num:
                min_num = numbers[num]
                res[length] += 1
            else:
                if res[length] < min_num:
                    res[length] += 1
                else:
                    res.append(1)
                    length += 1
                    min_num = numbers[num]
        else:
            res.append(1)
            length += 1
            min_num = numbers[num]
    return f'{len(res)}\n{" ".join(str(item) for item in res)}'


n = int(input())
for i in range(n):
    m = int(input())
    numbers = list(map(int, input().split()))
    print(search_min(numbers))
# print(search_min([1, 3, 3, 3, 2])) # 1 3 1
# print(search_min([7, 2, 3, 4, 3, 2, 7])) # 2 3 2 {[7, 2], [3, 4, 3], [2, 7]}
# print(search_min([1, 1, 9, 2, 9, 9, 9, 5, 8]))
# print(search_min([10, 9, 9, 10, 3, 4, 1, 8, 2, 7]))
# print(search_min([10, 10, 10, 1, 5, 8, 4, 8, 9, 8]))
# print(search_min([1, 3, 10, 4, 6, 4, 3, 7, 6, 10]))
# print(search_min([4, 3, 8, 3, 7, 1, 10, 5, 1, 4]))
# print(search_min([5, 2, 5, 5, 10, 10, 10, 1, 6, 3]))
# print(search_min([9, 2, 1, 4, 1, 9, 8, 3, 1, 1]))
# print(search_min([4, 1, 6, 4, 7, 1, 7]))
# print(search_min([2,  2]))
# print(search_min([1, 2]))
