# serversocket.py
import hmac
import hashlib
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)

def calcular_hmac(mensahe,clave,nonce):
     h = hmac.new(clave_secreta, mensaje.encode('utf-8'), hashlib.sha256)
     return h.hexdigest()

