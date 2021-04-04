
def create_output_string(month_range: list, average_month_prices: list) -> list:
    s_list = ['Date:        Average price ($): ']
    for c, i in enumerate(month_range):
        s_list.append(f'{i}      {average_month_prices[c]}')
    return s_list


class AveragePriceByMonth:
    """
    Calculates the monthly average prices for the given time period and given coin
    """
    def __init__(self, coin: str, month_range: list, data_array: list):
        self.sum = 0.0
        self.counter = 0
        self.average_month_prices = []
        for month in month_range:
            for data in data_array:
                if month == data["date"][:7] and data["coin"] == coin:
                    self.sum = self.sum + float(data["price"])
                    self.counter += 1
            if self.counter > 0:
                self.average_month_prices.append(round(self.sum / self.counter, 3))
                self.sum = 0
                self.counter = 0
        self.average_string = create_output_string(month_range, self.average_month_prices)
