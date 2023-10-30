import sqlite3
import hashlib
def crear_bd (lista_usuarios):
    conn = sqlite3.connect("users.db")
    conn.text_factory = str
    conn.execute("DROP TABLE IF EXISTS USUARIOS")
    conn.execute('''CREATE TABLE USUARIOS
    (NOMBRE TEXT NOT NULL,
    PASSWORD TEXT NOT NULL);''')
    for user, password  in lista_usuarios:
        hash = hashlib.sha256(password).hexdigest()
        
        conn.execute("INSERT INTO HASHES (NOMBRE,HASH) VALUES (?,?)",(user,password))

    