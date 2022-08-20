from parsing import StockParser
import pytest


def test_get_ticks_from_ids():

    # Case with customers
    r = StockParser.get_ticks_from_ids([
        {"_id": "TST1", "interested": [
            { "email": "test1@email.com", "max": 30, "min": None },
            { "email": "test2@email.com", "max": 33, "min": 13 }
        ]},
        {"_id": "TST2", "interested": [
            { "email": "test1@email.com", "max": 30, "min": None },
        ]}
    ])

    assert r == ["TST1", "TST2"]

    # Case with no customers
    r2 = StockParser.get_ticks_from_ids([{"_id": "TST1", "interested": []}])

    assert r2 == []

    # Case with no ticks
    r3 = StockParser.get_ticks_from_ids([])

    assert r3 == []


def test_stock_from_yfin():

    # Working case
    input = {'zip': '94043', 'sector': 'Communication Services', 'fullTimeEmployees': 174014, 'longBusinessSummary': 'Alphabet Inc. provides various products and platforms in the United States, Europe, the Middle East, Africa, the Asia-Pacific, Canada, and Latin America. It operates through Google Services, Google Cloud, and Other Bets segments. The Google Services segment offers products and services, including ads, Android, Chrome, hardware, Gmail, Google Drive, Google Maps, Google Photos, Google Play, Search, and YouTube. It is also involved in the sale of apps and in-app purchases and digital content in the Google Play store; and Fitbit wearable devices, Google Nest home products, Pixel phones, and other devices, as well as in the provision of YouTube non-advertising services. The Google Cloud segment offers infrastructure, platform, and other services; Google Workspace that include cloud-based collaboration tools for enterprises, such as Gmail, Docs, Drive, Calendar, and Meet; and other services for enterprise customers. The Other Bets segment sells health technology and internet services. The company was founded in 1998 and is headquartered in Mountain View, California.', 'city': 'Mountain View', 'phone': '650 253 0000', 'state': 'CA', 'country': 'United States', 'companyOfficers': [], 'website': 'https://www.abc.xyz', 'maxAge': 1, 'address1': '1600 Amphitheatre Parkway', 'industry': 'Internet Content & Information', 'ebitdaMargins': 0.34834, 'profitMargins': 0.25892, 'grossMargins': 0.56744, 'operatingCashflow': 95001001984, 'revenueGrowth': 0.126, 'operatingMargins': 0.29648, 'ebitda': 96886996992, 'targetLowPrice': 132, 'recommendationKey': 'strong_buy', 'grossProfits': 146698000000, 'freeCashflow': 51070373888, 'targetMedianPrice': 150, 'currentPrice': 118.12, 'earningsGrowth': -0.113, 'currentRatio': 2.809, 'returnOnAssets': 0.14927, 'numberOfAnalystOpinions': 10, 'targetMeanPrice': 148.95, 'debtToEquity': 11.28, 'returnOnEquity': 0.29216, 'targetHighPrice': 164.5, 'totalCash': 124997001216, 'totalDebt': 28810000384, 'totalRevenue': 278139011072, 'totalCashPerShare': 9.583, 'financialCurrency': 'USD', 'revenuePerShare': 21.03, 'quickRatio': 2.642, 'recommendationMean': 1.5, 'exchange': 'NMS', 'shortName': 'Alphabet Inc.', 'longName': 'Alphabet Inc.', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EDT', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-14400000', 'quoteType': 'EQUITY', 'symbol': 'GOOG', 'messageBoardId': 'finmb_29096', 'market': 'us_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 5.322, 'beta3Year': None, 'enterpriseToEbitda': 15.279, '52WeekChange': -0.16286027, 'morningStarRiskRating': None, 'forwardEps': 5.88, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 6162999808, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'totalAssets': None, 'bookValue': 19.53, 'sharesShort': 34674376, 'sharesPercentSharesOut': 0.0027, 'fundFamily': None, 'lastFiscalYearEnd': 1640908800, 'heldPercentInstitutions': 0.64485, 'netIncomeToCommon': 72016003072, 'trailingEps': 5.28, 'lastDividendValue': None, 'SandP52WeekChange': -0.056043804, 'priceToBook': 6.048131, 'heldPercentInsiders': 0.00039, 'nextFiscalYearEnd': 1703980800, 'yield': None, 'mostRecentQuarter': 1656547200, 'shortRatio': 1.1, 'sharesShortPreviousMonthDate': 1656547200, 'floatShares': 11360541360, 'beta': 1.078487, 'enterpriseValue': 1480310784000, 'priceHint': 2, 'threeYearAverageReturn': None, 'lastSplitDate': 1658102400, 'lastSplitFactor': '20:1', 'legalType': None, 'lastDividendDate': None, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': -0.136, 'priceToSalesTrailing12Months': 5.4961624, 'dateShortInterest': 1659052800, 'pegRatio': 1.73, 'ytdReturn': None, 'forwardPE': 20.088436, 'lastCapGain': None, 'shortPercentOfFloat': None, 'sharesShortPriorMonth': 35082340, 'impliedSharesOutstanding': 0, 'category': None, 'fiveYearAverageReturn': None, 'previousClose': 120.86, 'regularMarketOpen': 119.87, 'twoHundredDayAverage': 129.11343, 'trailingAnnualDividendYield': 0, 'payoutRatio': 0, 'volume24Hr': None, 'regularMarketDayHigh': 120, 'navPrice': None, 'averageDailyVolume10Day': 17032410, 'regularMarketPreviousClose': 120.86, 'fiftyDayAverage': 114.57269, 'trailingAnnualDividendRate': 0, 'open': 119.87, 'toCurrency': None, 'averageVolume10days': 17032410, 'expireDate': None, 'algorithm': None, 'dividendRate': None, 'exDividendDate': None, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 117.67, 'currency': 'USD', 'trailingPE': 22.371212, 'regularMarketVolume': 19516224, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 1528697192448, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 28629290, 'dayLow': 117.67, 'ask': 117.88, 'askSize': 1200, 'volume': 19516224, 'fiftyTwoWeekHigh': 152.1, 'fromCurrency': None, 'fiveYearAvgDividendYield': None, 'fiftyTwoWeekLow': 102.208, 'bid': 117.68, 'tradeable': False, 'dividendYield': None, 'bidSize': 800, 'dayHigh': 120, 'coinMarketCapLink': None, 'regularMarketPrice': 118.12, 'preMarketPrice': 119.92, 'logo_url': 'https://logo.clearbit.com/abc.xyz', 'trailingPegRatio': 1.7168}  # noqa
    r = StockParser.stock_from_yfin(input)
    assert r == {"_id": "GOOG", "name": 'Alphabet Inc.', "price": 118.12}

    # Missing keys
    with pytest.raises(KeyError):
        StockParser.stock_from_yfin(
            {'zip': '94043', 'sector': 'Communication Services'}
        )
