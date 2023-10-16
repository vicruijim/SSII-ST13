import hmac
import hashlib
import secrets
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

key = "123"

def crear_mensaje(m,clave):
     #nonce = os.urandom(16) #Calculamos el nonce
     nonce = secrets.token_hex(16) 
     h = hmac.new(key=clave.encode(), msg=m.encode('utf-8'), digestmod=hashlib.sha256) #calculamos el mac
     mac = h.hexdigest()#
     print(nonce)
     mensaje = str(m) + "|" + str(mac) + "|" + str(nonce)  
     return mensaje





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    while True:
        message = input("Escribe un mensaje (o 'exit' para salir): ")
        if message == 'exit':
            break
        cagao_de_sueño=crear_mensaje(message,clave= key)
        s.sendall(cagao_de_sueño.encode())
        data = s.recv(1024)
        print(f"Received {data!r}")

print("Conexión cerrada")
