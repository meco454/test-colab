import datetime
help(datetime.date)
date1 = datetime.date(2021,1,1)
date2 = datetime.date(day = 31,month = 7,year = 2021)
date3 = datetime.date(1990, month = 5, day = 7)
print(date1)
print(date2)
print(date3)


help(datetime.time)
t1 = datetime.time(12,0,0)
t2 = datetime.time(6,30,0)
t3 = datetime.time(9,15,0)

print(t1)
print(t2)
print(t3)


d1 = datetime.datetime(2020, 7, 20, 11, 30)
d2 = datetime.datetime(1990, 3, 10, 12)
d3 = datetime.datetime(2021, 1, 1)
print(d1)
print(d2)
print(d3)


str_d1 = "2020-07-21" 
str_d2 = "2020-12-31"
d1 = datetime.datetime.strptime(str_d1, "%Y-%m-%d")
d2 = datetime.datetime.strptime(str_d2, "%Y-%m-%d")


d3 = d2 - d1

print(f"Number of days: {d3.days}")



d1 = datetime.datetime.strptime("Jul 20 2020 11:30:00", "%b %d %Y %H:%M:%S")
d2 = datetime.datetime.strptime("2021-02-20 10:25:00", "%Y-%m-%d %H:%M:%S")
print(d2-d1)



d1 = datetime.datetime.strptime("2021-04-20 11:30:00", "%Y-%m-%d %H:%M:%S")

print(d1.strftime("%Y-%m-%d"))
print(d1.strftime("%d-%m-%Y"))
print(d1.strftime("%m-%Y"))
print(d1.strftime("%B-%Y"))
print(d1.strftime("%d %B, %Y"))
print(d1.strftime("%Y-%m-%d %H:%M:%S"))
print(d1.strftime("%m/%d/%y %H:%M:%S"))
print(d1.strftime("%d(%a) %B %Y"))



date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'
d1 = datetime.datetime.strptime(date_str_1, "%d %B %Y")
d2 = datetime.datetime.strptime(date_str_2, "%d/%m/%Y")
d3 = datetime.datetime.strptime(date_str_3, "%d-%m-%Y")

print(d1)
print(d2)
print(d3)



d1 = datetime.date.today()
d2 = datetime.date(d1.year, 12, 31)
print(f"Number of days until the end of the year: {(d2-d1).days}")



d1 = datetime.datetime.now()
d2 = datetime.datetime(d1.year, 12, 31)
print(f"Until the end of the year: {(d2-d1)}")



d1 = datetime.datetime(2020, 1, 1)
print(d1 + datetime.timedelta(days = 7))
print(d1 + datetime.timedelta(days = 30))
print(d1 + datetime.timedelta(hours = 30))
print(d1 + datetime.timedelta(minutes = 15))



dates = []
start_date = datetime.datetime(2020, 1, 1)
dates.append(start_date)
for index in range(12):
    print(dates[index])
    dates.append(dates[-1] + datetime.timedelta(hours = 8))

    


d1 = datetime.date(2021,7,1)
d2 = datetime.date(2021,12,31)
days_from = d2-d1
rate = 0.04
pv = 1000
print(days_from.days)
annual_converted = rate / days_from.days

value = pv * (1 + annual_converted) ** days_from.days
print(value)





d1 = datetime.date(2021,7,1)
d2 = datetime.date(2021,12,31)
days_from = d2-d1
rate = 0.04
pv = 1000
daily_rate = 0.04 / 365


for days in range (days_from.days):
    pv = pv + pv * daily_rate
print("Future value: $ %.2f" % pv)
