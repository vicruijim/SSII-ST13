import hashes
from datetime import datetime

def obtenerMAC(token, hashFichero):
    tokenStr = str(token)

    subHash = hashFichero[-10:len(hashFichero)]

    return str(tokenStr + subHash)

def calcularMACServer(token, hashFichero):
    hashesLocales = []
    with open(settings.rutaHashes, "r") as f:
        for line in f.readlines():
            strips = line.split(", ")

            hash = strips[1].strip()
            
            if (hash.strip() == hashFichero):
                hashesLocales.append(hash)

    if (len(hashesLocales) == 0):
        print("### ERRROR ###: file not found")
        return ""
    else:
        hash = str(hashesLocales[0])
        mac = obtenerMAC(token, hash)

    return str(mac)

# Parte del cliente

def enviarTokenServer(rutaFichero):
    hash = hashes.calcularHashArchivo(rutaFichero)
    mac1 = obtenerMAC(settings.tokenCliente, hash)

    mac2 = calcularMACServer(settings.tokenCliente, hash)

    if (mac1 != mac2):
        now = datetime.now()
        currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
        cadenaError = "[" + currentTime + "] Error in file: " + hash + ". Access denied\r\n"
        # escribir cadena de error en el archivo de errores

        with open(settings.rutaLogErrores, "w") as f:
            f.write(cadenaError)
