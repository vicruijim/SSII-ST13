import socket
import ssl


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    (client_socket, (client_ip, client_port)) = s.accept()
    print ("Connection accepted from %s:%s. Processing the request..." % (client_ip, client_port))
    conn = ssl.wrap_socket(client_socket, server_side=True, 
        certfile="./certificates/server.crt", keyfile="./certificates/server.key",
        ssl_version=ssl.PROTOCOL_TLSv1_3)
    print("Versión TLS utilizada:", conn.version())






"""
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
"""
