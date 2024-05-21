# n, k = map(int, input().split())
def get_timeslot(n, k):
    if k == 1: return ' '.join([str(i + 1) for i in range(n - 1)])
    if n == 2: return k
    dct = dict.fromkeys([_ for _ in range(1, n + 1)], {})
    updates_dict = dict.fromkeys([_ for _ in range(1, k + 1)], 0)
    count_updates_dict = dict.fromkeys([_ for _ in range(2, n + 1)], 0)
    for i in range(2, n + 1):
        dct[i] = {'updates': dict.fromkeys([_ for _ in range(1, k + 1)], 0),
                  'devices': dict.fromkeys([_ for _ in range(1, n + 1)], 0)}
    dct[1] = {'updates': dict.fromkeys([_ for _ in range(1, k + 1)], 1),
              'devices': dict.fromkeys([_ for _ in range(2, n + 1)], 0)}

    def get_devices2update() -> list:
        lst2update = []
        for i in range(2, n + 1):
            if count_updates_dict[i] < k:
                lst2update.append(i)
        return lst2update

    def get_min_update(device):
        updates = n
        min_update_number = n
        for j in range(1, k + 1):
            if dct[device]['updates'][j] == 0:
                tmp = updates_dict[j]
                if tmp < updates:
                    updates, min_update_number = tmp, j
                elif updates == tmp:
                    if j < min_update_number:
                        updates, min_update_number = tmp, j
        return min_update_number

    def download_from(part):
        min_downloads = k
        min_device_number = n
        for i in range(2, n + 1):
            if dct[i]['updates'][part] == 1:
                tmp = count_updates_dict[i]
                if tmp < min_downloads:
                    min_downloads, min_device_number = tmp, i
                elif min_downloads == tmp:
                    if i < min_device_number:
                        min_downloads, min_device_number = tmp, i
        return min_device_number

    def choose_device2update(device2download, devices):
        priority = 0
        priority_device = n
        downloads = k
        for device in devices:
            tmp = dct[device2download]['devices'][device]
            sum_downloads = count_updates_dict[device]
            if tmp > priority:
                priority, priority_device, downloads = tmp, device, sum_downloads
            elif tmp == priority:
                if sum_downloads < downloads:
                    priority, priority_device, downloads = tmp, device, sum_downloads
                elif sum_downloads == downloads:
                    if device < priority_device:
                        priority, priority_device, downloads = tmp, device, sum_downloads
        return priority_device

    res = []
    condition = 0
    counter = k
    n_tmp = [_ for _ in range(2, n + 1)] * k
    for i in range(k):
        dct[1]['devices'][n_tmp[i]] += 1
        dct[n_tmp[i]]['updates'][i + 1] += 1
        updates_dict[i + 1] += 1
        count_updates_dict[n_tmp[i]] += 1
        # print(f'slot {i + 1}')
        # print(f'device {n_tmp[i]} from 1 part {i + 1}')
    while condition != k * n:
        counter += 1
        dct2update = {}
        devices = get_devices2update()
        for device in devices:
            part2update = get_min_update(device)
            download_from_device = download_from(part2update)
            dct2update.setdefault(download_from_device, {}).setdefault(device, part2update)
        lst_priority = []
        for key, value in dct2update.items():
            if len(value) > 1:
                devices_lst = [key for key in value.keys()]
                priority_device = choose_device2update(key, devices_lst)
                part = dct2update[key][priority_device]
                lst_priority.append([priority_device, key, part])
            else:
                for priority_device, part in value.items():
                    lst_priority.append([priority_device, key, part])

        for j in lst_priority:
            dct[j[0]]['devices'][j[1]] += 1
            dct[j[0]]['updates'][j[2]] += 1
            updates_dict[j[2]] += 1
            count_updates_dict[j[0]] += 1
            # print(f'slot {counter}')
            # print(f'device {j[0]} from {j[1]} part {j[2]}')
            if sum(dct[j[0]]['updates'].values()) == k: res.append((str(counter), j[0]))
        condition = sum([sum(dct[i]['updates'].values()) for i in range(1, n + 1)])

    res.sort(key=lambda x: x[1])
    res = ' '.join([i[0] for i in res])
    return res
# # res = get_timeslot(n, k)
# res = get_timeslot(3, 30)
# print(res)
res = get_timeslot(3, 3)
print(res)
# res = get_timeslot(100, 35)
# print(res)
print('------')
res = get_timeslot(5, 10)  # 19 24 24 13
print(res)
print('------')
res = get_timeslot(2, 2) # 1
print(res)
res = get_timeslot(3, 1) #
print(res)
res = get_timeslot(3, 2) # 3 3
print(res)
print('------')
res = get_timeslot(4, 10) # 19 20 20
print(res)
print('------')
res = get_timeslot(2, 1)
print(res)
print('------')
res = get_timeslot(10, 10) #44 45 37 45 46 46 41 47 47
print(res)
print('------')
res = get_timeslot(20, 20) #159 157 140 124 160 161 154 161 149 152 160 155 132 162 150 162 158 163 163
print(res)
print('------')
res = get_timeslot(4, 4) #7 8 8
print(res)