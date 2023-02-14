import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue named 'hello' if it doesn't exist
channel.queue_declare(queue='hello')

msg = "A message from CS361"

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=msg)

print(f"Sending message: {msg}")

# Close the connection
connection.close()