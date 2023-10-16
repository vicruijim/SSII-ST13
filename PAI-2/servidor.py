# serversocket.py

import socket
import hmac
import hashlib
from datetime import datetime

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)

key="123"

mensajesIntegros = 0
totalmensajes = 0

def nonceUnico(nonce):
    with open("./nonces.txt", "rb") as nonces:
        for line in nonces:
            if (line.strip().decode() == nonce):
                print("Error: Nonce ya utilizado. Apuntando en log de errores...")

                with open("./logs/errors.log", "a") as errores:
                    now = datetime.now()
                    currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
                    errores.write(f" Detectado ataque reply a las {currentTime}, nonce ya registrado {nonce} \n")

                return False

    with open("./nonces.txt", "a") as writeNonces:
        writeNonces.write(nonce + "\n")

    return True


def calcular_hmac(mensaje,clave,nonce):
     
     if nonceUnico(nonce):
          h = hmac.new(clave.encode(), mensaje.encode('utf-8') , hashlib.sha256)
          return h.hexdigest()
     

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            if data:
                data = str(data)
                partes = data.split("|")
                mensaje = partes[0].strip()  
                mac = partes[1].strip() 
                nonce = partes[2].strip()
                print(mac) 
                macMensajeCalculado = calcular_hmac(mensaje.replace("b'",''), key,  nonce)
                print(macMensajeCalculado)
            if (str(macMensajeCalculado) == mac):
                    mensajesIntegros = mensajesIntegros + 1
                    
            else:
                    print("Error: Claves no coincidentes. Apuntando en el log de errores...")

                    with open("./logs/errors.log", "a") as errores:
                        now = datetime.now()
                        currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
                        errores.write(f"Posible ataque Man-in-the-middle a las {currentTime}. Mensaje afectado:{data}\n")
                    
            totalmensajes = totalmensajes + 1

            
        print("Conexión cerrada")




