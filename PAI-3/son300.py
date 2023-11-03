import threading
import socket
import ssl
PORT=3031
HOST ="localhost"
hilos = 2


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#ssl_context.minimum_version = ssl.TLSVersion.TLSv1_3
ssl_context.load_verify_locations('./certificado/servidor.crt')
mensaje ="Andres|pajaro|somos300"
def enviarMensaje():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with ssl_context.wrap_socket(s, server_hostname=HOST) as conn:
            conn.connect((HOST, PORT))
            conn.send(bytes(mensaje,'utf-8'))
            data = conn.recv(1024).decode("utf-8")

def atacad():
    
    for centinela in range(hilos):
        hilo = threading.Thread(name='Centinela %s' %centinela, 
                                target=enviarMensaje)
        hilo.start()

atacad()