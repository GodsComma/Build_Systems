"""
Recieve Quandle Data from Start Date to End Date
"""
import os
import datetime
import argparse
import quandl # type: ignore
#from typing import Callable

def main():
    '''
    Application Entry Point
    '''
    parser = argparse.ArgumentParser(description='''Recieve Stock Information for given Stock Name.
                                                    From a given start date to a given end date.
                                                 ''')
    parser.add_argument('-n', '--name', dest='stock_name',
                        type=str, help='Name of Stock', default=None)
    parser.add_argument('-s', '--startdate', dest='stock_startdate',
                        type=str, help='Start Date for the Sock Info', default=None)
    parser.add_argument('-e', '--enddate', dest='stock_enddate',
                        type=str, help='End Date for Stock Info', default=None)

    args = parser.parse_args()
    args = [arg for arg in vars(args) if getattr(args, arg) is not None]
    run(*args)

#def call_default_func(function: Callable, args: str) -> None:
   # '''
   # Call the function will no args if args param contain None
   # '''
   # for arg, position in enumerate(vars(args)):
   #     if arg is None:
   #         delattr(args, arg)
   # print("*"*20)
   # print(function(*args))
   # print("*"*20)
   # function(*args)

def run(stock: str = 'EOD/AAPL', start_date: str = "", end_date: str = "") -> None:
    '''
    CLI EntryPoint
    '''
    old = 365*4

    start_date = validate_date(start_date, default=old+7)
    end_date = validate_date(end_date, default=old)
    try:
        quandl.ApiConfig.api_key = load_api_key()
        data = quandl.get(stock, start_date=start_date, end_date=end_date)
        print(data)
        return data
    except ValueError as run_exception:
        print(f"{run_exception}")
        return None

def validate_date(date: str = "", default: int = 0) -> str:
    '''
    Validate a datetime string
    '''
    if date == "":
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=default)
        date = (now - delta).date().strftime("%Y-%m-%d")
    return date

def load_api_key() -> str:
    '''
        Loads Quandl API key from environment variables
    '''
    quandl_api_key = os.environ.get('API_KEY', None)
    if quandl_api_key is None:
        raise ValueError("Value Error: (ENV_VAR) Missing API_KEY, Add Quandl API_KEY")
    return quandl_api_key
