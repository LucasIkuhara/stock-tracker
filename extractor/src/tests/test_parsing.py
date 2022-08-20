from parsing import StockParser


def test_get_ticks_from_ids():

    # Case with customers
    r = StockParser.get_ticks_from_ids([
        {"_id:": "TST1", "interested": [
            { "email": "test1@email.com", "max": 30, "min": None },
            { "email": "test2@email.com", "max": 33, "min": 13 }
        ]}
    ])

    assert r == "TST1"

    # Case with no customers
    r2 = StockParser.get_ticks_from_ids([{"_id:": "TST1", "interested": []}])

    assert r2 == []

    # Case with no ticks
    r3 = StockParser.get_ticks_from_ids([])

    assert r3 == []
