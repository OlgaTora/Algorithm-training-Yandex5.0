k = int(input())


def get_ship_size(k):
    def check_size(num):
        condition = num * (num + 1) * (num + 2) // 6
        return True if condition + num * (num + 1) // 2 - 1 <= k else False

    l, r = 0, k
    while l < r:
        num = (l + r + 1) // 2
        if check_size(num):
            l = num
        else:
            r = num - 1
    return l


print(get_ship_size(k))

# print(get_ship_size(117055765888857794)) #888887
# print(get_ship_size(400)) #11
# print(get_ship_size(1)) #1
