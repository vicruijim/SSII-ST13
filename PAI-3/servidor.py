import socket
import ssl


#HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 3031  # Port to listen on (non-privileged ports are > 1023)
HOST= "0.0.0.0"

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='./cert_remoto/servidor.crt', keyfile='./cert_remoto/servidor.key')
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        conn = ssl_context.wrap_socket(conn, server_side=True)  # Aplicar SSL a la conexión
        with conn:
            print('Conexión aceptada de:', addr)

            # Trabaja con la conexión como lo necesites
            conn.send(b'Bienvenido al servidor seguro con TLS 1.3\n')
            data = conn.recv(1024)
            print('Datos recibidos:', data.decode())

