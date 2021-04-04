import json
import csv


class CreateJsonCSV:
    """
    Class that manages the creation of files
    """
    def __init__(self, data_array, coin, f_format, name):
        self.array = data_array
        self.coin = coin
        if f_format == "json":
            self.exportJson(name)
        elif f_format == "csv":
            self.exportCSV(name)
        else:
            pass

    def exportJson(self, name) -> None:
        """
        Exporting the json file with the given name
        """
        try:
            name = str(name)
            with open(name, 'w') as file:
                json.dump(self.array, file)
        except:
            print("Export json error!")

    def exportCSV(self, name) -> None:
        """
        Exporting the csv file with the given name
        """
        try:
            with open(name, 'w') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Date', 'Price', self.coin])
                for dictionary in self.array:
                    writer.writerow([dictionary["date"], dictionary["price"], dictionary["coin"]])
        except:
            print("Export CSV error!")
