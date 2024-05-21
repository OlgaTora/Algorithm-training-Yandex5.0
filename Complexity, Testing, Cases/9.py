quantity = int(input())
year = int(input())
holidays = [input() for i in range(quantity)]
first_weekday = input()
from datetime import datetime
import calendar

wdays = list(calendar.day_name)
wdays_num = range(1, 8)
month_dict = dict(zip(wdays_num, wdays))

dct = {}
days = 366 if calendar.isleap(year) else 365
for d in range(1, days + 1):
    wday = datetime.strptime(str(d) + '.' + str(year), '%j.%Y').isoweekday()
    dct[wday] = dct.get(wday, 0) + 1
for hol in holidays:
    hol = ' '.join([hol, str(year)])
    hol = datetime.strptime(hol, '%d %B %Y')
    wday = hol.isoweekday()
    dct[wday] = dct.get(wday, 0) - 1
res = max(dct, key=dct.get)
res_ = min(dct, key=dct.get)
print(month_dict.get(res) + ' ' + month_dict.get(res_))
