import pika
import json
import sys


def validation_format(format_in):
    format_list = ['csv', 'table', 'xml', 'json']

    if format_in in format_list:
        return format_in

    else:
        print (" Wrong type " + format_in + " . You should insert csv, table, xml, json ")
        sys.exit(0)


def send_massage():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()


    ############################################################
    ###### Please Set db_path and data_format ##################
    ############################################################

    body = json.dumps({'db_path': '/home/stas.r/Downloads/chinook.db' ,
                       'data_format' : validation_format('csv')})



    channel.queue_declare(queue='messageQunene')


    channel.basic_publish(exchange='', routing_key='messageQunene', body=body)
    connection.close()


send_massage()





