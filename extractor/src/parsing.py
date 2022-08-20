from typing import List


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

        return []
