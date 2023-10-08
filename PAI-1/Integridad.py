from hashes import *
from datetime import datetime, timedelta
import schedule
import time

def ver_hashes(dir):
    list_ficheros = os.listdir(dir)
    cambio = False
    conn = sqlite3.connect("hashes.db")
    conn.text_factory=str
    cursor = conn.execute("SELECT * FROM HASHES")
    datos_bd = cursor.fetchall()
    if len(list_ficheros) < len(datos_bd):
         for dato in datos_bd:
              if dato[0] not in list_ficheros:
                     cambio = True
                     print(f"El archivo {dato[0]}")
                     with open("./Logs/Logs.txt", "a") as archivo:
                        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        archivo.write(f"El archivo {dato[0]} ha sido borrado {hora}\n")   
                    
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
    #schedule.every().day.at("02:00").do(ver_hashes, "./integridad") #codigo para realizar la comprobacion cada dia a las 02:00
    dia = datetime.now().day
    if dia == 1: # comprobar si es nuevo mes
         informe_mensual()
         with open("./Logs/Logs.txt", "w") as archivo: #Borrar el fichero logs
            pass  
    schedule.every(2).seconds.do(ver_hashes, "./integridad")#prueba frecuencia cada 5 s
    schedule.every(60).seconds.do(informe_mensual)
    # Ejecuta la programación
    while True:
        schedule.run_pending()
        time.sleep(1)

# Funcion que genera el informe mensual
def informe_mensual():
     ultimoDiaMesAnterior=datetime.today().date().replace(day=1) - timedelta(days=1)
     mes = ultimoDiaMesAnterior.month
     anyo = ultimoDiaMesAnterior.year
     with open("./Logs/Logs.txt", "r") as origen, open(f"./Reporte/Informe-{mes}-{anyo}.txt", "w") as destino:
         destino.write(f"Informe del mes:{mes} año:{anyo}\n")
         contenido = origen.read()  
         destino.write(contenido) #Se copia contenido de logs al reporte 

   
          
          

if __name__ == "__main__":
    #comprobacion_diaria()
    informe_mensual()