from sys import getsizeof
from myLib import *
import socket

def recv():
    total=b""
    receiver=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    PORT=int(input("Enter receiver's port: "))
    receiver.bind(("",PORT))
    i=0
    while(True):
        recved, senderInfo=receiver.recvfrom(1024)
        print(getsizeof(recved))
        i+=1

        if recved==b"stop" or recved==b"exit" :
                break

        total+=recved

        print("Received {} bytes".format(len(total)))
    with open(input("Save as: "),"wb") as file:
        file.write(total)
