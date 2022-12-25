import pika

credentials = pika.PlainCredentials(username='andres', password='holivin12andres')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
for x in range(100000):
    channel.basic_publish(exchange='', routing_key='hello', body=str(x))

print(" [x] Sent 'Hello World!'")
connection.close()
