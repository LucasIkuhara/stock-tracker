from distutils.log import info
from utils import get_db_connection
from parsing import StockParser
from sys import argv
import yfinance as yf


# Get collection from caller
try:
    collection = argv[1]
except:
    raise Exception("Missing Collection name. Aborting.")

# Open Db connection and get all ticks that must be fetched
conn = get_db_connection()
res = conn['tracked-stocks'][collection].find({})
tick_names = StockParser.get_ticks_from_ids(list(res))
print(tick_names)

# Fetch info for the ticks
# !REFACTOR
ticks = yf.Tickers(" ".join(tick_names))

for tick in ticks.tickers:
    info = ticks.tickers[tick].info
    
    try:
        stock = StockParser.stock_from_yfin(info)
        conn['tracked-stocks'][collection].insert_one(stock)
    
    except KeyError:
        print(f'Missing info or invalid stock: {tick}')
        continue

res = conn['tracked-stocks'][collection].find({})
