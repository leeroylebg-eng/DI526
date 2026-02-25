from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    print(datetime(now.year + 1, 1, 1) - now)

time_until_new_year()