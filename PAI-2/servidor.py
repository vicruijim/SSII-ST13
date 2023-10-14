# serversocket.py
import hmac
import hashlib
import socket

nonces_utilizados = set()

def calcular_hmac(mensaje,clave,nonce):
     h = hmac.new(clave, mensaje.encode('utf-8'), hashlib.sha256)
     return h.hexdigest()




HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)
