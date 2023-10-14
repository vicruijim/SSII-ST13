import hmac
import hashlib
import os
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

def calcular_hmac(mensaje,clave,nonce):
     

def crear_mensaje(mensaje):
     nonce = os.urandom(16) #Calculamos el nonce 
     h = hmac.new(key=key.encode(), mensaje.encode('utf-8'), hashlib.sha256) #calculamos el mac
     mac = h.hexdigest()#
     enviar = 





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    
    client_socket.connect((HOST, PORT))

    mensaje = "Este es un mensaje de prueba."
    nonce = generar_nonce()
    hmac_calculado = calcular_hmac(mensaje, nonce)

    mensaje_con_hmac = f"{mensaje}|{hmac_calculado}|{nonce.hex()}"

    client_socket.sendall(mensaje_con_hmac.encode())

    print("Mensaje enviado al servidor.")
