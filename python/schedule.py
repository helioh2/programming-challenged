
def date_order(x):
    days = "Mon Tue Wed Thu Fri Sat Sun".split()
    x1, x2 = x.split(" ")
    print(x1, x2)
    return days.index(x1), x2

def to_minutes(time):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)
    return hours*60 + minutes


def difference(date1, date2):
    days = "Mon Tue Wed Thu Fri Sat Sun".split()
    day1, times1 = date1.split(" ")
    day2, times2 = date2.split(" ")
    if day1 == "Sun" and day2 == "Mon":
        return 0  #can't sleep from Sun to Mon
    day_difference = days.index(day2) - days.index(day1)
    end_time_first = to_minutes(times1.split("-")[-1])
    begin_time_next = to_minutes(times2.split("-")[0])
    relative_difference = (begin_time_next - end_time_first) % (24*60)
    if day_difference > 1:
        difference = relative_difference + (24*60) * (day_difference - 1)
    else:
        difference = relative_difference
    return difference

def solution(S):

    # write your code in Python 3.6
    lines = S.split("\n")
    print(lines)
    time_slots = []
    lines.sort(key = date_order)
    print(lines)
    max_slot = 0
    for k in range(len(lines)-1):
        first = lines[k]
        next = lines[k+1]
        slot = difference(first, next)
        if slot > max_slot:
            max_slot = slot

    last = lines[-1]
    slot = difference(last, "Sun 24:00-24:00")
    if slot > max_slot:
        max_slot = slot

    return max_slot





#
#
# #main
# x = solution('''Sun 10:00-20:00
# Fri 05:00-10:00
# Fri 16:30-23:50
# Sat 10:00-24:00
# Sun 01:00-04:00
# Sat 02:00-06:00
# Tue 03:30-18:15
# Tue 19:00-20:00
# Wed 04:25-15:14
# Wed 15:14-22:40
# Thu 00:00-23:59
# Mon 05:00-13:00
# Mon 15:00-21:00''')
#
#
# print(x)


x = solution('''Mon 01:00-23:00
Tue 01:00-23:00
Wed 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Sat 01:00-23:00
Sun 01:00-21:00''')


print(x)