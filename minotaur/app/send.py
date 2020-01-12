#!/usr/bin/env python
'''
    This is the publisher

'''
import pika
import sys, logging

def publish(option, message):
    # Connect to RabbitMQ on the localhost, if different machine use IP/hostname
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', connection_attempts=5, retry_delay=5, heartbeat=300))
    channel = connection.channel()

    #'test' exchange to send the message to
    channel.exchange_declare(exchange='test', exchange_type='direct', passive=False, durable=True, auto_delete=False)

    channel.basic_publish(exchange='test', routing_key=option, body=message)

    print(" [x] Sent %r:%r" % (option, message))

    channel.close()

option = sys.argv[1] if len(sys.argv) >2 else 'info'
message = ' '.join(sys.argv[1:])

publish(option, message)
