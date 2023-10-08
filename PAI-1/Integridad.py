from hashes import *
from datetime import datetime
import schedule
from datetime import datetime
import time

def ver_hashes(dir):
    list_ficheros = os.listdir(dir)
    cambio = False
    conn = sqlite3.connect("hashes.db")
    conn.text_factory=str
    cursor = conn.execute("SELECT * FROM HASHES")
    serranito = cursor.fetchall()
    if len(list_ficheros) < len(serranito):
         for alioli in serranito:
              if alioli[0] not in list_ficheros:
                     cambio = True
                     print(f"El archivo {alioli[0]}")
                     with open("./Logs/Logs.txt", "a") as archivo:
                        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        archivo.write(f"El archivo {alioli[0]} ha sido borrado {hora}\n")   
                    
    for fichero in list_ficheros:
        hash = calcula_hash("./"+dir+"/"+fichero)
        cursor = conn.execute("SELECT NOMBRE FROM HASHES WHERE HASH = ?",(hash,))
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
#ver_hashes("./integridad")

def comprobacion_diaria():
    # Programa la comprobación diaria para ejecutarse todos los días a una hora específica
    #schedule.every().day.at("02:00").do(ver_hashes, "./integridad") #frecuencia diaria
    schedule.every(5).seconds.do(ver_hashes, "./integridad")#prueba frecuencia cada 5 s
    # Ejecuta la programación
    while True:
        schedule.run_pending()
        time.sleep(1)

# Ejecuta la función para programar la comprobación diaria
def informe_mensual():
     pass

if __name__ == "__main__":
    comprobacion_diaria()
