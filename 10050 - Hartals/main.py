from sys import stdin

def readnum():
    return int(stdin.readline())

def readcase():
    days = readnum()
    nparties = readnum()
    
    return days, [readnum() for _ in range(nparties)]

def is_holiday(day):
    return day%7 == 6 or day%7 == 5

def count_hartals(days, parties):

    # Mark all hartals
    calendar = [0 for _ in range(days)]

    for p in parties:
        current = p
        while current <= days:
            calendar[current-1] = 1
            current += p

    
    # remove holidays
    for d in range(days):
        if is_holiday(d):
            calendar[d] = 0

    # Count hartal days
    return sum(calendar)


if __name__ == '__main__':

    ncases = readnum()

    for c in range(ncases):
        days, parties = readcase()
        print(count_hartals(days, parties))
