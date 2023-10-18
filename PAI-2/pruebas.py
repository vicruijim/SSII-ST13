import socket
HOST = "127.0.0.1"
PORT = 3030

def ejecutarAtaque():
    msg = str(input("Introduzca un mensaje a enviar al servidor: "))
    nonce = str(input("Introduzca el nonce del mensaje: "))
    mac = str(input("Introduzca la mac del mensaje: "))

    mensaje = (msg + "|" + mac + "|" + nonce)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        soc.send(mensaje.encode())
    print("Enviado correctamente. Saliendo...")

ejecutarAtaque()