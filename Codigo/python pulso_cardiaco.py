import time
import board
import busio
import adafruit_max30102
import datetime
import csv

# Inicialización del sensor MAX30102
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_max30102.MAX30102(i2c)

# Archivo CSV para almacenar los datos
archivo_csv = "datos_pulso_cardiaco.csv"

# Función para escribir datos en el archivo CSV
def escribir_en_csv(tiempo, pulso):
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tiempo, pulso])

# Bucle principal
try:
    print("Iniciando la monitorización del pulso cardíaco...")
    while True:
        # Lee la frecuencia cardíaca del sensor
        pulso = sensor.read

        # Obtiene la fecha y hora actual
        tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Imprime y guarda en el archivo CSV
        print(f"{tiempo_actual} - Frecuencia cardíaca: {pulso} BPM")
        escribir_en_csv(tiempo_actual, pulso)

        # Espera 1 minuto antes de la próxima lectura
        time.sleep(60)

except KeyboardInterrupt:
    print("Programa detenido por el usuario")

finally:
    # Limpia los recursos al finalizar
    sensor.shutdown()
