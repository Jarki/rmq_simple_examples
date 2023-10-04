import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

exchange_name = "exchange_events"

exchange = channel.exchange_declare(exchange_name, exchange_type='topic')

channel.queue_bind(queue_name, exchange_name, '#')

print(f"[*] Waiting for messages in exchange {exchange_name}. Press Ctrl+C to cancel.")

def print_consumed(ch, method, properties, body):
    print(f"[+] TOPIC: {method.routing_key} MESSAGE: {body}")

channel.basic_consume(queue_name, print_consumed, auto_ack=True)
channel.start_consuming()