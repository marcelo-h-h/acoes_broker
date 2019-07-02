import zmq

class Subscriber():
    """
    The subscriber is the entity which receives messages from the publisher and filter it by a specific topic
    In this case, subscribers filter messages based on the stock they're determinated, the message contains the new values
    of the stock and the subscriber send it to a monitor
    """
    def __init__(self, back_port: int, stock: str, monitor_port: int):
        port = str(back_port)
        topicfilter = stock

        # Socket to talk to server
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB) # Create the sub socket from which it gets the new values
        print ("Collecting updates from server...")
        self._socket.connect("tcp://localhost:%s" % port) # Connect to the backend port of the forwarder
        self._socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter) # Set the topic to filter the messages (stock)

        port = str(monitor_port)
        self._push_socket = self._context.socket(zmq.PUSH) # Creates the push socket which connects to the monitor
        self._push_socket.connect("tcp://localhost:%s" % port) # Connect to the monitor port

    def run(self):
        try:
            while True:
                string = self._socket.recv() # Receives message from the forwarder
                topic, messagedata = string.split()
                self._push_socket.send(messagedata) # Send the message to the monitor
                #print(messagedata, 'utf-8') # uncomment this line to get the messages sent to each sub
        
        except:
            print('Shutting down sub')
        finally:
            self._socket.close()
            self._push_socket.close()
            self._context.term()

def start_new_sub(back_port: int, stock: str, monitor_port: int):
    s = Subscriber(back_port, stock, monitor_port)
    s.run()