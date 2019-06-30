import sys
import zmq

class Subscriber():
    def __init__(self, back_port: int, stock: str):
        port = str(back_port)
        # Socket to talk to server
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        print ("Collecting updates from server...")
        self._socket.connect ("tcp://localhost:%s" % port)
        topicfilter = stock
        self._socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

    def run(self):
        try:
            while True:
                string = self._socket.recv()
                topic, messagedata = string.split()
                print (topic, messagedata)
        
        except KeyboardInterrupt:
            self._context.term()
            print('Shutting down sub')

def start_new_sub(back_port: int, stock: str):
    s = Subscriber(back_port, stock)
    s.run()