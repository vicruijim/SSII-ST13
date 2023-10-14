import hmac
import hashlib
import os
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

def crear_mensaje(m,clave):
     nonce = os.urandom(16) #Calculamos el nonce 
     h = hmac.new(key=clave.encode(), msg=mensaje.encode('utf-8'), digestmode=hashlib.sha256) #calculamos el mac
     mac = h.hexdigest()#
     mensaje = m + "|" + mac + "|" + nonce  
     return mensaje





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    
    client_socket.connect((HOST, PORT))

    mensaje = str(input("Introduzca un mensaje a enviar al servidor: "))
    clave = str(input("Introduzca la clave privada: "))

    mensaje_hmac = crear_mensaje(mensaje,clave)

    client_socket.sendall(mensaje_hmac.encode())

    print("Mensaje enviado al servidor.")
