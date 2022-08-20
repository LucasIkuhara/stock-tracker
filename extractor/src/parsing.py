from typing import List, Dict


class StockParser:

    @staticmethod
    def get_ticks_from_ids(stocks_array) -> List[str]:
        '''
        Get a list of ticks from a list of stocks formatted as dicts.
        Their structure should follow the pattern:
        {"_id:": "TICK1", "interested": [...]}

        Arguments:
            stocks_array: an array of objects with stock ticks as their _id.

        Returns:
            A list of stock ticks as str. 
        '''

        result = filter(lambda obj: len(obj["interested"]) > 0, stocks_array)
        result = map(lambda obj: obj["_id"], result)
        result = list(result)

        return result 

    @staticmethod
    def stock_from_yfin(obj: Dict) -> Dict:
        '''
        Takes in a dict structured as an yfinance tick info object and formats it as
        a stock document, ready to be stored.

        Arguments:
            obj: The input dict.

        Returns:
            A dict representing a stock ready to be stored.

        Raises:
            KeyError: in case the entry is missing a required attribute.
        '''

        pass
