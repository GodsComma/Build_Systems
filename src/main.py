"""
Recieve Quandle Data from Start Date to End Date
"""
import os
import datetime
import quandl # type: ignore

def main():
    '''
    Application Entry Point
    '''
    run()

def run(stock: str = 'EOD/AAPL', start_date: str = "", end_date: str = "") -> None:
    '''
    CLI EntryPoint
    '''
    old = 365*4

    start_date = validate_date(start_date, default=old+7)
    end_date = validate_date(end_date, default=old)

    quandl.ApiConfig.api_key = load_api_key()
    data = quandl.get(stock, start_date=start_date, end_date=end_date)
    print(data)
    return data

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
    assert quandl_api_key is not None
    return quandl_api_key
