
import socket
import ssl

#HOST = "localhost"  # The server's hostname or IP address
PORT = 3031  # The port used by the server
HOST= "DESKTOP-NE5LGKC"

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_3
ssl_context.load_verify_locations(cafile='./cert_remoto/servidor.crt')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with ssl_context.wrap_socket(s, server_hostname=HOST) as conn:
        conn.send(b'Hola, servidor seguro con TLS 1.3\n')
        data = conn.recv(1024)
        print('Respuesta del servidor:', data.decode())

        user = input("Usuario:")
        password = input("Contraseña:")
        msj = input("Mensaje:")
        datos = (user + "|" + password + "|"+ msj)
        conn.send(datos.encode)