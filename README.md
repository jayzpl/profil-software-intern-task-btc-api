Profil Software Recruitment task - backend internship
This script process historical data from external API about cryptocurrencies and give desirable results.

Required libraries:
- PyMongo 
- Click 
- Dnspython
- Coinpaprika
- Tests

Available commands:
python script.py [command] [paremeters]

1. python script.py --help
  Shows available commnads
  
2. python script.py [command] --help
  Shows available parameters for the command 
 
3. python script.py average-price-by-month
  Shows the average prices for the month over a period of time

4. python script.py consecutive-increase
  Shows the longest period of price increase in the given time period and the value by which the prices have increased

5. python script.py export
  Exports date and price data to a json or csv file with the given name

If no parameters are given, the command will be executed for default values

Avialable parameters:
1. [parameter]=[value]

2. --start-date
  Sets the start date of the time range
  Default: 2021-01-01
  
3. --end-date
  Sets the end date of the time range
  Default: 2021-04-01
 
4. --coin
  Sets what currency we will be testing
  Default: btc-bitcoin

Only available for the export command:

5. --format
  Sets the file format to be exported
  Default: csv
  
6. --file
  Sets a name for the exported file
  Default: export.csv
  
Examples:

- python script.py average-price-by-month --start-date=2020-01-01 --end-date=2020-06-01 --coin=usdt-tether
Shows the average value of prices in the range from 2020-01-01 to 2020-06-01 for the usdt-tether currency.

- python script.py export --start-date=2020-01-01 --end-date=2020-06-01 --format=json --file=file.json --coin=usdt-tether
Exports data from 2020-01-01 to 2020-06-01 such as date and currency price to a file in the json format named file.json for usdt-tether currency

Digression:
- If data for a given period of time and for a given currency exist in the database, the program will not download them again from the api.
- I used the mongodb database because it can be useful when using json files.
- Before testing the program, it is best to use the delete_all_data method from the db class to delete all data from the database.
