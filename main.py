""" Main script """
# Python Standard library
import sys
import time
import datetime
import argparse
import logging

# ThirdParty Libs
import pyRofex

# Local modules
from client import TraderClient

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


if __name__ == '__main__':
    """Main module"""

    has_bid = False
    bid_first_prices = 0
    order_price = 0

    # Collect params
    parser = argparse.ArgumentParser()
    parser.add_argument("-T", "--ticker", help="Ticker of asset", type=str, required=True)
    parser.add_argument("-u", "--user", help="Username (reMarkets)", type=str, required=True)
    parser.add_argument("-p", "--password", help="Password (reMarkets)", type=str, required=True)
    args = parser.parse_args()
    user = args.user
    password = args.password
    instrument = args.ticker

    # Inicialize
    trader = TraderClient(user=user, password=password)

    trader.open_connection()

    logging.info("Consultando símbolo")
    # Set entries
    entries = [pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.LAST]
    md = trader.get_market_data(instrument, entries)

    if md["status"] != "ERROR":

        # LP or Last Price
        last_price = md["marketData"]["LA"]
        if last_price:
            logging.info("Último precio operado: ${}".format(last_price["price"]))

        # BIDS
        logging.info("Consultando BID")
        bids = md["marketData"]["BI"]
        if len(bids) > 0:
            logging.info("Precio de BID: ${}".format(bids[0].get("price")))
            bid_first_prices = md["marketData"]["BI"][0]["price"]
            has_bid = True
        else:
            logging.warning("No hay BIDs activos")

        # Define precio de orden
        order_price = (bid_first_prices - 0.01) if has_bid else 75.25
        trader.send_order(instrument, order_price)
    else:
        logging.error("Símbolo inválido")

    trader.close_connection()



