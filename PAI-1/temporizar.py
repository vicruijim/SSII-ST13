import schedule
import time
from datetime import datetime
from Integridad import *
# Importa la función ver_hashes y otras dependencias aquí

def comprobarDiariamente(dir, log_dir):
    def job():
        print("Realizando comprobación diaria...")
        ver_hashes(dir)
        print("Comprobación diaria completada.")

        # Obtiene la fecha y hora actual
        now = datetime.now()

        # Comprueba si ha comenzado un nuevo mes
        if now.day == 1:
            # Se ha iniciado un nuevo mes, crea un nuevo archivo de informe
            mes_anio = now.strftime("%B %Y")
            informe_path = f"{log_dir}/{mes_anio}_informe.log"
            with open(informe_path, "w") as log:
                log.write(f"Informe del mes de {mes_anio}\n")
                log.write(f"Fecha y hora de la comprobación: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
                log.write("Resultado de la comprobación diaria:\n")
                # Puedes agregar más información si lo deseas.

        # Abre el archivo de informe mensual y agrega los registros diarios
        with open(informe_path, "a") as log:
            log.write(f"Fecha y hora de la comprobación: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
            log.write("Resultado de la comprobación diaria:\n")
            # Puedes agregar más información sobre la actividad diaria si lo deseas.

    # Programa la tarea para que se ejecute todos los días a una hora específica, por ejemplo, a las 2 AM.
    schedule.every().day.at("02:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Ejemplo de uso:
if __name__ == "__main__":
    directorio_a_comprobar = "./tu_directorio"  # Reemplaza con la ruta de tu directorio
    directorio_logs = "./logs"  # Reemplaza con la ruta de tu directorio de logs
    comprobarDiariamente(directorio_a_comprobar, directorio_logs)
