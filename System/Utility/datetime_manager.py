import datetime

class DatetimeManager():
    
    def get_current_date():
        return datetime.datetime.now().date()

    def get_current_time():
        return datetime.datetime.now().time().strftime("%I:%M %p")
    
    def compare_dates(date1, date2):
        date_format = "%Y-%m-%d"

        d1 = datetime.datetime.strptime(date1, date_format).date()
        d2 = datetime.datetime.strptime(date2, date_format).date()

        # Compare the dates
        if d1 < d2:
            return -1
        elif d1 > d2:
            return 1
        else:
            return 0
