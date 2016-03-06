import datetime

def StillPrep(TodayIs):

    while TodayIs == datetime.date.today():
        continue
    return False

