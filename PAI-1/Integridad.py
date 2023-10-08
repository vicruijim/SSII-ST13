from hashes import *
from datetime import datetime
import schedule
from datetime import datetime
import time
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
            hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            with open("./Logs/Logs.txt", "a") as archivo:
                 archivo.write(f"El archivo {fichero} ha sido modificado {hora}\n")
        
    if cambio:
        almacenar_fichero(dir)
    else: 
            print("Los ficheros siguen igual")
    conn.close()
ver_hashes("./integridad")

def comprobacion_diaria():
    # Programa la comprobación diaria para ejecutarse todos los días a una hora específica
    schedule.every().day.at("02:00").do()  # Llama a la función desde el otro archivo

    # Ejecuta la programación
    while True:
        schedule.run_pending()
        time.sleep(1)

# Ejecuta la función para programar la comprobación diaria
if __name__ == "__main__":
    comprobacion_diaria()
   