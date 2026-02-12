import databento as db
import pandas as pd

company = pd.read_csv('top20_sp500_tech_companies.csv')
company['识别号'] = company['交易所'].apply(lambda x: 'XNAS.ITCH' if x.upper() == 'NASDAQ' else 'XNYS.ITCH') # XNAS.ITCH = Nasdaq; XNYS.ITCH = NYSE

API_KEY = "API_Key" # Enter your API key

client = db.Historical(API_KEY)

data = client.timeseries.get_range(
    dataset="XNAS.ITCH", # XNAS.ITCH = Nasdaq; XNYS.ITCH = NYSE
    schema="ohlcv-1s",
    symbols=["AAPL"], # Company name
    start="2025-10-28T20:00:00Z",  # UTC Time
    end="2025-10-28T23:00:00Z"
)

df = data.to_df()
print(df.head())