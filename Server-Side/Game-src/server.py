import socket
import threading
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",2700))


clients = []
address = []
i=0
s.listen(5)
print "server initialized"
while i<=1:
    print "waiting for client"
    c,a = s.accept()
    print "recieved connection from player ",a
    clients.append(c)
    address.append(a)
    i+=1

def player_one():
        while True:
               buffer_player_one = clients[0].recv(1024)
               if len(buffer_player_one) >0:
                   clients[1].send(buffer_player_one)
def player_two():
    while True:
            buffer_player_two = clients[1].recv(1024)
            if len(buffer_player_two) >0:
                clients[0].send(buffer_player_two)


threading.Thread(target = player_one).start()
threading.Thread(target = player_two).start()
