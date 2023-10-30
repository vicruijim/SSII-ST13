import socket
import ssl

# Configura la dirección del servidor y el puerto al que se conectará el proxy
SERVER_HOST = '192.168.181.45'
SERVER_PORT = 3031

def proxy_client(client_socket):
    # Crea una conexión SSL hacia el servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((SERVER_HOST, SERVER_PORT))
    while True:
        # Recibe datos del cliente
        client_data = client_socket.recv(4096)
        if not client_data:
            break

        # Reenvía datos al servidor
        server_socket.send(client_data)

        # Recibe datos del servidor
        server_data = server_socket.recv(4096)
        if not server_data:
            break

        # Reenvía datos al cliente
        client_socket.send(server_data)

    client_socket.close()
    server_socket.close()

def start_proxy():
    # Configura el servidor proxy
    HOST = '0.0.0.0'
    PORT = 3030  # Puerto al que se conectará el cliente

    # Crea un socket del servidor
    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server.bind((HOST, PORT))
    proxy_server.listen(5)

    print(f"Proxy escuchando en {HOST}:{PORT}")

    while True:
        # Espera una conexión del cliente
        client_socket, client_addr = proxy_server.accept()
        print(f"Conexión aceptada de {client_addr}")

        # Inicia un hilo para manejar la comunicación del cliente
        proxy_thread = threading.Thread(target=proxy_client, args=(client_socket,))
        proxy_thread.start()

if __name__ == '__main__':
    import threading
    start_proxy()
