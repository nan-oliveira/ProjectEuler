'''
<p>You are given the following information, but you may prefer to do some research for yourself.</p>
<ul><li>1 Jan 1900 was a Monday.</li>
<li>Thirty days has September,<br />
April, June and November.<br />
All the rest have thirty-one,<br />
Saving February alone,<br />
Which has twenty-eight, rain or shine.<br />
And on leap years, twenty-nine.</li>
<li>A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.</li>
</ul><p>How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?</p>
'''

def get_number_of_sun():
    ini = 0
    count = 0
    for year in range(1901, 2001):
        for month in countMonths.keys():
            # get the day of the week. And adds 1 case of leap year
            index = (ini + 1 + ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))) % 7
            # sum days for different months
            ini = index + ((countMonths[month] - 1) % 7)

            day_week = week[index]
            if day_week == 'sun':
                count += 1
    return count

week = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
countMonths = {
 'jan':31,
 'feb':28,
 'mar':31,
 'apr':30,
 'may':31,
 'jun':30,
 'jul':31,
 'aug':31,
 'sep':30,
 'oct':31,
 'nov':30,
 'dec':31
}

def get_number_of_sun():
    ini = 2
    count = 0
    for year in range(1901, 2001):
        for month in countMonths.keys():
            # get the day of the week. And adds 1 case of leap year
            countMonths['feb'] = 29 if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else 28

            index = ini % 7
            # sum days for different months
            ini = index + (countMonths[month] % 7)

            day_week = week[index]
            if day_week == 'sun':
                count += 1

            #print('year: ', year, 'month: ', month, 'Index: ', index, day_week)
    return count

print(get_number_of_sun())