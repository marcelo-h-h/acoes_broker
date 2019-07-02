import zmq
import time
import pprint


class Monitor():
    def __init__(self, monitor_port: int):
        port = str(monitor_port)
        self._context = zmq.Context()
        self._receiver = self._context.socket(zmq.PULL)
        self._receiver.bind("tcp://*:%s" % port)
        self._stocks = {}
        #print("Starting monitor listening at tcp://localhot:%s" % port)

    def run(self):
        try:
            while True:
                msg = self._receiver.recv_string()
                stock, value, variation = msg.split("_")
                _value_str, value = value.split(':')
                value = float(value)
                print(stock)
                if stock in self._stocks:
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
                print('Stocks:')
                pprint.pprint(self._stocks)
                

        except Exception as e:
            print(str(e))
            print('Shutting down monitor with errors')
        finally:
            self._receiver.close()
            self._context.term()

def start_new_monitor(monitor_port: int):
    m = Monitor(monitor_port)
    m.run()


 