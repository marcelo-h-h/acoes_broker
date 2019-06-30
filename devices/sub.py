import sys
import zmq

port = "8888"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print ("Collecting updates from server...")
socket.connect ("tcp://localhost:%s" % port)
topicfilter = "9"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
for update_nbr in range(10):
    string = socket.recv()
    topic, messagedata = string.split()
    print (topic, messagedata)