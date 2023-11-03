import threading
import socket
import ssl

# Configuración del servidor
HOST = "localhost"
PORT = 3031
datos= "LATIA|ABUELA|ABUELETE"
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_3
ssl_context.load_verify_locations(cafile='./certificado/servidor.crt')  # Ajusta la ruta de tu archivo de certificado

# Función para establecer una conexión SSL con el servidor
def establecer_conexion():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        with ssl_context.wrap_socket(s, server_hostname=HOST) as conn:
            print(f'Conexión establecida con {HOST}:{PORT}')
            print(datos)
            conn.send(datos.encode())
# Número de conexiones que deseas abrir
num_conexiones = 300

# Crear hilos para establecer conexiones
threads = []
for i in range(num_conexiones):
    t = threading.Thread(target=establecer_conexion)
    threads.append(t)
    t.start()

# Esperar a que todos los hilos terminen
for t in threads:
    t.join()
