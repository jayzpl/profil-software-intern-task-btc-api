from pymongo import MongoClient


class DB:
    def __init__(self):
        """
        Set connection with mongodb database
        """
        try:
            self.cluster = MongoClient(
                "")
            self.db = self.cluster["btc_db"]
            self.collection = self.db["btc_db"]
        except:
            print("Database connection error!")

    def download_data(self, coin: str) -> list:
        """
        Gets data of chosen coin from the database and places it in an data array.
        Accepts coin value
        """
        _cursor = self.collection.find()
        data_array = []
        for i in _cursor:
            if i["coin"] == coin:
                dictionary = {"date": i["date"], "price": i["price"], "coin": i["coin"]}
                data_array.append(dictionary)
            else:
                pass
        return data_array

    def upload_new_data(self, data_array: list, coin: str) -> None:
        """
        Uploads only those data that are not in the database
        Accepts data array from api and coin
        """
        _db_array = self.download_data(coin)
        _is_data_in_db = False
        try:
            for i in data_array:
                for j in _db_array:
                    if i["date"] == j["date"] and i["coin"] == j["coin"]:
                        _is_data_in_db = True
                if not _is_data_in_db:
                    self.collection.insert_one(i)
                _is_data_in_db = False
        except:
            print("Data insert failed !")

    def is_date_range_in_db(self, date_array: list, coin: str) -> bool:
        """
        Returns true if data of chosen coin and time range are in database
        """
        _data_array = self.download_data(coin)
        first_date, second_date = False, False
        if len(_data_array) > 0:
            for i in _data_array:
                if i["date"] == date_array[0] and i["coin"] == coin:
                    first_date = True
                if i["date"] == date_array[len(date_array) - 1] and i["coin"] == coin:
                    second_date = True
        if first_date and second_date:
            return True
        else:
            return False

    def delete_all_data(self):
        self.collection.delete_many({})
