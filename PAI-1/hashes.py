import hashlib 
import os 
import sqlite3

def calcula_hash(fichero):
    try:
        hash_sha256 = hashlib.sha256()
        with open(fichero, "rb") as archivo:
            for bloque in iter(lambda: archivo.read(4096), b""): #b"" condicion para que finalice el bucle al encontrarse una cadena de bytes vacia 
                hash_sha256.update(bloque)
        return hash_sha256.hexdigest()
    except FileNotFoundError:
        return "El archivo no se encontró."
    except Exception as e:
        return f"Error: {e}"


def almacenar_fichero(dir):
    conn = sqlite3.connect("hashes.db")
    conn.text_factory = str
    conn.execute("DROP TABLE IF EXISTS HASHES")
    conn.execute('''CREATE TABLE HASHES
    (NOMBRE TEXT NOT NULL,
    HASH TEXT NOT NULL);''')
    for fichero in os.listdir(dir):
        hash = calcula_hash("./"+dir+"/"+fichero)
        cursor = conn.execute("""INSERT INTO HASHES (NOMBRE,HASH) VALUES 
        (?,?)""",(fichero,hash))
    conn.commit()
    cursor = conn.execute("SELECT * FROM HASHES")
    print(cursor.fetchall())
    conn.close()
 
c = False
if c:
    almacenar_fichero("./integridad")
        


