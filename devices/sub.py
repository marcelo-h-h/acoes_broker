import zmq

class Subscriber():
    def __init__(self, back_port: int, stock: str, monitor_port: int):
        port = str(back_port)
        topicfilter = stock

        # Socket to talk to server
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        print ("Collecting updates from server...")
        self._socket.connect("tcp://localhost:%s" % port)
        self._socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

        self._ncontext = zmq.Context()
        port = str(monitor_port)
        self._push_socket = self._ncontext.socket(zmq.PUSH)
        self._push_socket.connect("tcp://localhost:%s" % port)
        #print("Listening at tcp://localhost:%s" % monitor_port)

    def run(self):
        try:
            while True:
                string = self._socket.recv()
                topic, messagedata = string.split()
                self._push_socket.send(messagedata)
        
        except:
            print('Shutting down sub')
        finally:
            self._socket.close()
            self._push_socket.close()
            self._context.term()
            self._ncontext.term()

def start_new_sub(back_port: int, stock: str, monitor_port: int):
    s = Subscriber(back_port, stock, monitor_port)
    s.run()