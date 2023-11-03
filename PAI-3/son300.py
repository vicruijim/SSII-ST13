import threading
import socket
import ssl
PORT=3031
HOST ="localhost"
hilos = 1
mensaje = "Andres|pajaro|somos300"

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_3
#ssl_context.load_verify_locations(cafile='./cert_remoto/servidor.crt')
ssl_context.load_verify_locations(cafile='./certificado/servidor.crt')

def enviarMensaje():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        with ssl_context.wrap_socket(s, server_hostname=HOST) as conn:
            dato = mensaje
            print(dato)
            conn.send(dato.encode())

def atacad():
    
    for centinela in range(hilos):
        hilo = threading.Thread(name='Centinela %s' %centinela, 
                                target=enviarMensaje)
        hilo.start()

atacad()