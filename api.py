from coinpaprika import client as cp


def set_returned_array(data: list, coin) -> list:
    """
    From downloaded data returns array with dates and prices of chosen coin
    """
    returned_array = []
    for i in data:
        dictionary = {"date": i["time_close"][:10], "price": i["close"], "coin": coin}
        returned_array.append(dictionary)
    return returned_array


class LoadDataFromApi:
    """
    Set connection with API, download data of chosen time range and coin, sets the desired values to
    array. It accepts 3 strings
    """
    def __init__(self, coin: str, start_date: str, end_date: str):
        try:
            self.client = cp.Client()
            self.data_array = set_returned_array(self.download_data(coin, start_date, end_date), coin)
        except:
            print("API Connection error!")

    def download_data(self, coin: str, start_date: str, end_date: str) -> list:
        return self.client.candles(coin, start=start_date, end=end_date)
