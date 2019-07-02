import zmq
import random
import time

class Server():
    """
    The server is the publisher, it has a stock associated with him and constantly generates a new
    variation of the stock price and publishes it to the forwarder, and consequently,to the subs
    """
    def __init__(self, front_port: int, stock: str, stock_value: float):
        self._stock = stock
        self._value = stock_value
        port = str(front_port)
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.PUB) # Defines its sockets as a pub type socket
        self._socket.connect("tcp://localhost:%s" % port) # Bind the socket to the frontend port of the forwarder
        
    def run(self):
        try:
            while True:
                negative = -1 if random.random()>=0.5 else 1 # Decides whether the variation will be positive or negative
                variation = random.random() * 0.01 * negative # Decides the variation value
                self._value += self._value * variation # Sets up the new value
                messagedata = "Stock:%s" % self._stock + "_Value:%f" %self._value + "_Variation:%f" %(variation*100) +"%" # Mount up the message about the stock
                self._socket.send_string("%s %s" % (self._stock, messagedata)) # Sends the message through the socket
                time.sleep(1)

        except:
            print('Shutting down server')
        finally:
            self._socket.close()
            self._context.term()

def start_new_server(front_port: int, stock: str, stock_value: float):
    s = Server(front_port, stock, stock_value)
    s.run()

