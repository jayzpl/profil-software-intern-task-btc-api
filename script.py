"""Profil Software Recruitment task - backend internship
    created by Jakub Zasada
    contact emial: jzasada06@gmail.com
    Date: 2021-04-04"""

import click
import data
import average_price
import con_increase
import export_file


def show(s_list: str):
    for i in s_list:
        print(i)


@click.group()
def commands():
    pass


@commands.command()
@click.option('--start-date', default="2021-01-01")
@click.option('--end-date', default="2021-04-01")
@click.option('--coin', default="btc-bitcoin")
def average_price_by_month(start_date, end_date, coin):
    """
    Average price by month command. Shows average price by month for given coin and time period.
    If there are no parameters, use the default parameters
    """
    data_array, days_range, months_range = data.data_management(start_date, end_date, coin)
    avg_price = average_price.AveragePriceByMonth(coin, months_range, data_array)
    show(avg_price.average_string)


@commands.command()
@click.option('--start-date', default="2021-01-01")
@click.option('--end-date', default="2021-04-01")
@click.option('--coin', default="btc-bitcoin")
def consecutive_increase(start_date, end_date, coin):
    """
    Consecutive increase command. Shows the longest period of time the price increases for given coin and time
    period. If there are no parameters, use the default parameters
    """
    data_array, days_range, months_range = data.data_management(start_date, end_date, coin)
    increase = con_increase.Increase(days_range, coin, data_array)
    show(increase.increase_string)


@commands.command()
@click.option('--start-date', default="2021-01-01")
@click.option('--end-date', default="2021-04-01")
@click.option('--coin', default="btc-bitcoin")
@click.option('--format', default="csv")
@click.option('--file', default="export.csv")
def export(start_date, end_date, coin, format, file):
    """
    Export command. Creates a file of the selected format with data on the selected coin and the selected time
    period. If there are no parameters, use the default parameters
    """
    api_data = data.export_to_file(start_date, end_date, coin)
    export_file.CreateJsonCSV(api_data, coin, format, file)


if __name__ == "__main__":
    commands()
