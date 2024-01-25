import yfinance as yf
import json
import pandas as pd
import datetime
import os
import yaml
import time

def get_options_data(ticker_data, ticker, data_directory):
    exp_dates = ticker_data.options
    options_data = {}
    for date in exp_dates:
        opt = ticker_data.option_chain(date)
        options_data[date] = {
            'calls': opt.calls.apply(lambda x: x.apply(lambda y: y.isoformat() if isinstance(y, pd.Timestamp) else y), axis=1).to_dict('records'),
            'puts': opt.puts.apply(lambda x: x.apply(lambda y: y.isoformat() if isinstance(y, pd.Timestamp) else y), axis=1).to_dict('records')
        }
    write_to_json(options_data, ticker, "options", data_directory)
    return True



def write_to_json(data, ticker, dataset_name, data_directory):
    date_str = datetime.datetime.now().strftime("%Y_%m_%d")
    filename = f"{ticker}_{dataset_name}_{date_str}.json"
    directory = os.path.join(data_directory, ticker, dataset_name)
    full_path = os.path.join(directory, filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_tickers_from_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_ticker_data(ticker):
    return yf.Ticker(ticker)

# Main execution
if __name__ == "__main__":
    start_time = time.time()
    
    # uncomment dev while testing
    # ENV = "PROD"
    ENV = "DEV"
    
    if ENV == "PROD":
        yaml_file_path = 'tickers.yaml'
        data_directory = 'financial_data'
    else:
        yaml_file_path = 'tickers_exp.yaml'
        data_directory = 'test_data'

    tickers = read_tickers_from_yaml(yaml_file_path)

    for ticker in tickers:
        ticker_data = get_ticker_data(ticker)
        get_options_data(ticker_data, ticker, data_directory)
        print(f"Data downloaded for -> {ticker}")
        time.sleep(0.5)

    elapsed_time = time.time() - start_time
    print(f"The program took {elapsed_time} seconds to run.")
