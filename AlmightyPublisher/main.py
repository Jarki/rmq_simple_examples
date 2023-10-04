import time
import json

import pika

from order_manager_interface import order_types


conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()

exchange_name = "test_165271"

# ex = channel.exchange_declare(exchange_name, exchange_type='topic')

order = order_types.BalanceInfo()
# order = order_types.MarketOrder("BTCUSDT", "sell", 0.01)
# order = order_types.LimitOrder("BTCUSDT", "sell", 0.01, 30_000)
# order = order_types.StopLimitOrder("BTCUSDT", "buy", 0.01, 30_002, 30_000)

# order = order_types.SingleOrderCancel("BTCUSDT", 10322910)
# order = order_types.MultiOrderCancel("BTCUSDT")

body = order.to_json()

# body = json.dumps({
#     'timestamp': time.time(),
#     'price': 30
# })

# topic = 'a.b.new_price'
# topic = 'a.b.order_operations'
topic = "hola.bruh.test_12"

# body = ""

channel.basic_publish(exchange_name, topic, body=body)