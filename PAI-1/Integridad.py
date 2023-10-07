from hashes import *
#import time

def ver_hashes(dir):
    conn = sqlite3.connect("hashes.db")
    conn.text_factory=str
    for fichero in os.listdir(dir):
        hash = calcula_hash("./"+dir+"/"+fichero)
        cursor = conn.execute("SELECT * FROM HASHES")
        a = cursor.fetchone()
        if a == None:
            print("se ha modificado el archivo")
        else: 
            print("El fichero sigue igual")
    conn.close()
ver_hashes("./integridad")

    