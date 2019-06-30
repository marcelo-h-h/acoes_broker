import zmq



def main():

    port_sub = "8087"
    port_pub = "8888"

    
    context = zmq.Context()
    #Socket dos subscribers
    conexao_subs = context.socket(zmq.SUB)
    conexao_subs.bind("tcp://*:%s" % port_sub)
    conexao_subs.setsockopt_string(zmq.SUBSCRIBE, "")


    #Socket dos publishers
    conexao_pubs = context.socket(zmq.PUB)
    conexao_pubs.bind("tcp://*:%s" % port_pub)
    
    zmq.device(zmq.FORWARDER, conexao_subs, conexao_pubs)


    conexao_pubs.close()
    conexao_subs.close()
    context.term()
        


if __name__ == "__main__":
    main()