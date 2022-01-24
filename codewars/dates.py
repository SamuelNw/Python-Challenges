from datetime import date, timedelta

def period_is_late(last,today,cycle_length):
    diff = (today - last).days
    if diff > cycle_length:
        return True
    return False


print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28))

