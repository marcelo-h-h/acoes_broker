import zmq


class Broker_acoes():
    def __init__(self, front_port: int, back_port: int):
        context = zmq.Context()
        conexao_subs = context.socket(zmq.SUB)
        conexao_pubs = context.socket(zmq.PUB)

        try:
            #Socket dos subscribers
            conexao_subs.bind("tcp://*:%s" % front_port)
            conexao_subs.setsockopt_string(zmq.SUBSCRIBE, "")

            #Socket dos publishers
            conexao_pubs.bind("tcp://*:%s" % back_port)
            
            zmq.device(zmq.FORWARDER, conexao_subs, conexao_pubs)


        except:
            print('Shutting down broker')    
        finally:
            conexao_pubs.close()
            conexao_subs.close()
            context.term()

def start_new_broker(front_port: int, back_port: int):
    broker = Broker_acoes(front_port, back_port)