sec_in_day = 86400
sec_in_hour = 3600
sec_in_minute = 60

duration = int (input ('Введите значение: '))

d = duration // sec_in_day
duration = duration - (d * sec_in_day)

h = duration // sec_in_hour
duration = duration - (h * sec_in_hour)

m = duration // sec_in_minute

s = duration - (m * sec_in_minute)

print (d, 'дней', h, 'час', m , 'мин', s , 'сек')