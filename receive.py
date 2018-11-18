import pika
import json
import main as m



def receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='messageQunene')

    def callback(ch, method, properties, body):

        data = json.loads(body)
        m.main(data['db_path'],data['data_format'])


    channel.basic_consume(callback, queue='messageQunene', no_ack=True)

    print('waiting for messages')
    channel.start_consuming()

receive()




