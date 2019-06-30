import sys
import zmq

class Subscriber():
    def __init__(self, back_port: int, stock: str):
        port = str(back_port)
        topicfilter = stock

        # Socket to talk to server
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        print ("Collecting updates from server...")
        self._socket.connect ("tcp://localhost:%s" % port)
        self._socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

    def run(self):
        try:
            while True:
                string = self._socket.recv()
                topic, messagedata = string.split()
                print (topic, messagedata)
        
        except:
            print('Shutting down sub')
        finally:
            self._socket.close()
            self._context.term()

def start_new_sub(back_port: int, stock: str):
    s = Subscriber(back_port, stock)
    s.run()