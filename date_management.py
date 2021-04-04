from datetime import datetime, timedelta


def create_date_from_string(start_date: str, end_date: str):
    """
    Returns dates in the datetime format
    """
    try:
        start_date_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_date = datetime.strptime(end_date, '%Y-%m-%d')
        return start_date_date, end_date_date
    except:
        print("Input date syntax error. Preferred format: Y-m-d")


def is_date_valid(start_date: datetime, end_date: datetime) -> bool:
    if start_date > end_date:
        return False
    else:
        return True


def create_days_range(start_date: datetime, end_date: datetime) -> list:
    delta_time = end_date - start_date
    days_array = []
    for i in range(delta_time.days + 1):
        day = start_date + timedelta(days=i)
        day = day.strftime('%Y-%m-%d')
        days_array.append(day)
    return days_array


def create_months_range(days_range_array: list) -> list:
    months_array = []
    for i in days_range_array:
        if i[:7] in months_array:
            pass
        else:
            months_array.append(i[:7])
    return months_array


class DateRange:
    def __init__(self, start_date_str: str, end_date_str: str):
        """
        Sets two arrays with days and months range
        """
        start_date, end_date = create_date_from_string(start_date_str, end_date_str)
        if is_date_valid(start_date, end_date):
            self.days_range_array = create_days_range(start_date, end_date)
            self.months_range_array = create_months_range(self.days_range_array)
        else:
            raise Exception
