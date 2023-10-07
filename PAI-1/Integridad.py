from hashes import *
#import time

def ver_hashes(dir):
    
    cambio = False
    conn = sqlite3.connect("hashes.db")
    conn.text_factory=str
    for fichero in os.listdir(dir):
        hash = calcula_hash("./"+dir+"/"+fichero)
        cursor = conn.execute("SELECT * FROM HASHES WHERE HASH = ?",(hash,))
        a = cursor.fetchone()
        if a == None:
            cambio = True
            #añadir el fichero al Log
            with open("./Logs/Logs.txt", "w") as archivo:
                 archivo.write(f"El archivo {fichero} ha sido modificado \n")
        
    if cambio:
        almacenar_fichero(dir)
        
    else: 
            print("Los ficheros siguen igual")
    conn.close()
ver_hashes("./integridad")

    