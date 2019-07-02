import zmq
import time
import os



class Monitor():
    """
    The monitor is a device which gets info of all the stocks from the subs and use them to construct
    historical data about their variation
    On the model, the monitor is a device used for traders to decide upon the history of a stock if they
    should buy or sell determinated stock (Quite a simple tradding model)
    """
    def __init__(self, monitor_port: int):
        port = str(monitor_port) 
        self._context = zmq.Context()
        self._receiver = self._context.socket(zmq.PULL) # The monitor has a PULL type socket to get the messages with new values from subs
        self._receiver.bind("tcp://*:%s" % port) # The monitor is bind to a port where subs send their value updates messages
        self._stocks = {} # The stocks are displayed in a JSON style

    def run(self):
        try:
            while True:
               
                msg = self._receiver.recv_string() # Receives the message from subs
                stock, value, variation = msg.split("_")
                _value_str, value = value.split(':')
                value = float(value)

                # Mounts the JSON with historical data about the stocks and their values
                if stock in self._stocks.keys():
                    self._stocks[stock]['curr_value'] = value
                    if self._stocks[stock]['high_value'] < value:
                        self._stocks[stock]['high_value'] = value
                    if self._stocks[stock]['low_value'] > value:
                        self._stocks[stock]['low_value'] = value
                else:
                    self._stocks[stock] = {}
                    self._stocks[stock]['curr_value'] = value
                    self._stocks[stock]['high_value'] = value
                    self._stocks[stock]['low_value'] = value
                
                #print('Stocks:')
                os.system('clear') # Constantly clears the screen so it looks more dynamic
                print(self._stocks) # Print the JSON style display
                

        except Exception as e: # Error treatment
            print(e)
            print('Shutting down monitor')
        finally:
            self._receiver.close()
            self._context.term()


def start_new_monitor(monitor_port: int):
    m = Monitor(monitor_port)
    m.run()


 