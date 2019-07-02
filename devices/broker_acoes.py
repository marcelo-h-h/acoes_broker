import zmq


class Broker_acoes():
    """
    The broker is a forwarder device, which is the device that serves as an stable intermediary between
    publishers and subscribers
    As the name says, it forward the messages from pubs to subs
    """
    def __init__(self, front_port: int, back_port: int):
        context = zmq.Context() # Gets zmq context
        conexao_subs = context.socket(zmq.SUB) # set the socket to which pubs send their messages
        conexao_pubs = context.socket(zmq.PUB) # Set the socket from which subs get their messages

        try:
            # Subscribers socket
            conexao_subs.bind("tcp://*:%s" % front_port)
            conexao_subs.setsockopt_string(zmq.SUBSCRIBE, "")

            # Publishers socket
            conexao_pubs.bind("tcp://*:%s" % back_port)

            # Generate the forwarder device, with its proper sockets
            zmq.device(zmq.FORWARDER, conexao_subs, conexao_pubs)


        except: 
            print('Shutting down broker')    
        finally:
            conexao_pubs.close()
            conexao_subs.close()
            context.term()

def start_new_broker(front_port: int, back_port: int):
    broker = Broker_acoes(front_port, back_port)