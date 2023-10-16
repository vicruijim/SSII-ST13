import hmac
import hashlib
import os
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

key = "123"

def crear_mensaje(m,clave):
     nonce = os.urandom(16) #Calculamos el nonce 
     h = hmac.new(key=clave.encode(), msg=m.encode('utf-8'), digestmode=hashlib.sha256) #calculamos el mac
     mac = h.hexdigest()#
     mensaje = m + "|" + mac + "|" + nonce  
     return mensaje





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    while True:
        message = input("Escribe un mensaje (o 'exit' para salir): ")
        if message == 'exit':
            break
        crear_mensaje(message,clave= key)
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Received {data!r}")

print("Conexión cerrada")
