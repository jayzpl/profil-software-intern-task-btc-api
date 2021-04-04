import date_management
import input_data
import api

"""
Create datetime object from given string
"""


def test_create_date_from_string():
    start_date = "2020-01-01"
    end_date = "2021-01-01"
    start, end = date_management.create_date_from_string(start_date, end_date)
    assert start
    assert end


"""
When the first date is earlier than the second
"""


def test_is_date_valid():
    start_date = "2020-01-01"
    end_date = "2021-01-02"
    start, end = date_management.create_date_from_string(start_date, end_date)
    result = date_management.is_date_valid(start, end)
    assert result


"""
Whether all inputs are strings
"""


def test_input_data_is_valid():
    result = input_data.is_valid("string", "string", "string")
    assert result


"""
When some data is not a string
"""


def test_input_data_is_not_valid():
    result = input_data.is_valid("string", 1, True)
    assert not result


"""
Connect to api and get data into array
"""


def test_load_data_from_api():
    # given
    coin = "btc-bitcoin"
    start_date = "2020-01-01"
    end_date = "2020-01-02"
    api_data = api.LoadDataFromApi(coin, start_date, end_date)

    assert len(api_data.data_array) != 0
