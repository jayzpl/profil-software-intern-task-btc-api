import api
import db
import input_data
import date_management


def data_management(start_date: str, end_date: str, coin: str):
    """
    Manages the data. Checks and valid the input data.
    Returns data from the database for the selected time
    interval, returns array of days and months range
    """
    if input_data.is_valid(start_date, end_date, coin):
        days_range = date_management.DateRange(start_date, end_date).days_range_array
        months_range = date_management.DateRange(start_date, end_date).months_range_array
        if db.DB().is_date_range_in_db(days_range, coin):
            db_data_array = db.DB().download_data(coin)
            return db_data_array, days_range, months_range
        else:
            api_data = api.LoadDataFromApi(coin, start_date, end_date)
            db.DB().upload_new_data(api_data.data_array, coin)
            return data_management(start_date, end_date, coin)
    else:
        print("Input data are not valid!")
        return [],[],[]


def export_to_file(start_date: str, end_date: str, coin: str):
    """
    Returns api data for the exported file
    """
    if input_data.is_valid(start_date, end_date, coin):
        date_management.DateRange(start_date, end_date)
        api_data = api.LoadDataFromApi(coin, start_date, end_date)
        return api_data.data_array
    else:
        print("Input data are not valid!")
        return []
