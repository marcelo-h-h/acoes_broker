import zmq
import random
import sys
import time

class Server():
    def __init__(self, front_port: int, stock: str, stock_value: float):
        self._stock = stock
        self._value = stock_value
        port = str(front_port)
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.PUB)
        self._socket.connect("tcp://localhost:%s" % port)
        
    def run(self):
        try:
            while True:
                negative = -1 if random.random()>=0.5 else 1
                variation = random.random() * 0.1 * negative
                self._value += self._value * variation
                messagedata = "Stock:%s" % self._stock + "-Value:%i" %self._value + "-%f" %variation
                #print ("%s %s" % (self._stock, messagedata))
                self._socket.send_string("%s %s" % (self._stock, messagedata))
                time.sleep(1)

        except KeyboardInterrupt:
            self._context.term()
            print('Shutting down server')

def start_new_server(front_port: int, stock: str, stock_value: float):
    s = Server(front_port, stock, stock_value)
    s.run()

