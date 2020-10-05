"""trader client"""
# Python Standard library
import sys
import logging

# ThirdParty Libs
import pyRofex


class TraderClient:
    """
    Trader Client Class
    """
    ACCOUNT = "REM5029"

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.account = self.ACCOUNT

    def open_connection(self):
        """estabilsh connection"""
        logging.info("Iniciando sesión en Remarkets")
        try:

            pyRofex.initialize(
                user=self.user,
                password=self.password,
                account=self.account,
                environment=pyRofex.Environment.REMARKET
            )
        except Exception as e:
            logging.critical("No se pudo establecer conexion con ROFEX")

    def send_order(self, ticker, order_price):
        """ send order"""
        logging.info("Ingresando orden a ${}".format(order_price))
        try:
            order = pyRofex.send_order(ticker=ticker,
                                       side=pyRofex.Side.BUY,
                                       size=10,
                                       price=order_price,
                                       order_type=pyRofex.OrderType.LIMIT)

            #estado Orden
            order_status = self.get_order_status(order)
            logging.info("Estado orden:")
            logging.info("Status: {}".format(order_status["status"]))
            logging.info("Order ID: {}".format(order_status["order"]["orderId"]))
            logging.info("Descripción: {}".format(order_status["order"]["text"]))

        except Exception as e:
            logging.error("No se pudo enviar la orden")

    def get_order_status(self, order):
        """ returns order status"""
        return pyRofex.get_order_status(order["order"]["clientId"])

    def get_market_data(self, ticker, entries):
        """ retrieve market data"""
        return pyRofex.get_market_data(ticker, entries, depth=2)

    def close_connection(self):
        """estabilsh connection"""
        logging.info("Cerrando sesión en Remarkets")
