class Increase:
    """
    Class that measures the longest price increases of given time period
    """
    def __init__(self, days_range_array: list, coin: str, data_array: list):
        self.new_data_array = []
        self.increase = []
        for day in days_range_array:
            for data in data_array:
                if day == data["date"] and data["coin"] == coin:
                    self.new_data_array.append(data)
        self.increase_string = self.con_increase()

    def con_increase(self) -> list:
        """
        Returns array with string of the longest price increase
        """
        if len(self.new_data_array) != 0:
            first_price = float(self.new_data_array[0]["price"])
            last_price = float(self.new_data_array[0]["price"])
            first_date = self.new_data_array[0]["date"]
            last_date = ""
            period, value = 0, 0
            # We check that the price of the next date is not lower than the price of the previous one
            for i in self.new_data_array:
                if float(i["price"]) >= last_price:
                    last_date = i["date"]
                    last_price = float(i["price"])
                    period += 1
                else:
                    delta_price = last_price - first_price
                    self.increase.append(
                        {"from": first_date, "to": last_date, "delta": round(delta_price, 2), "period": period})
                    first_price = float(i["price"])
                    last_price = first_price
                    first_date = i["date"]
                    last_date = first_date
                    period = 0
            for counter, j in enumerate(self.increase):
                if float(j["period"]) > value:
                    value = float(j["period"])
                    which = counter
            s_list = [
                f'Longest increase period from {self.increase[which]["from"]} to {self.increase[which]["to"]} with '
                f'increase of: ${self.increase[which]["delta"]}']
            return s_list
