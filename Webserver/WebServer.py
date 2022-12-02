import socket
import config
from function.MethodParse import *
from threading import Thread
# tiep nhan cac request tu client gui ve
def Method(client):
    while True:
        request=getRequest(client)
        if not request:
            break
        if not request.empty:
            if request.content != '':
                print(f"-------------------\n [LISTENED REQUEST]\n Request catched: %s with %s has content %s\n"%(request.method, request.path, request.content))
            else:
                print(f"-------------------\n [LISTENED REQUEST]\n Request catched: %s with %s \n"%(request.method, request.path))
            if request.method == "POST":
                postMethod(client, request)
                client.shutdown(socket.SHUT_RD)
            else:
                getMethod(client, request)
                client.shutdown(socket.SHUT_RD)
    client.shutdown(socket.SHUT_RD)

# chia thread de tiep nhan cac connections khac nhau
def Connections():
    while True:
        (client,address)=server.accept()
        print(f"-------------------\n [SERVER]\n Listening request from {address}")
        Thread(target=Method,args=(client,)).start()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind((config.HOST, config.PORT))
print(f'* Running on http://{config.HOST}:{config.PORT}')
print(f'          or http://{config.IP}:{config.PORT}')

try:
    server.listen(5) # cho phep lang nghe toi da 5 ket noi cung luc
    ACCEPT_THREAD=Thread(target=Connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
except:
    print("error\n")
finally:
    server.close()
 	
