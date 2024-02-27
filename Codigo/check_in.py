#Modelo base de Health-In-Motion
from gpiozero import LED, DistanceSensor
from datetime import datetime
import RPi.GPIO as GPIO
import time

#Sensores base con 2 LED y el sensor de proximidad
sensor = DistanceSensor(echo = 21, trigger = 20)
verde = LED(13)
amarillo = LED(6)

#Desactivar los warnings (optional)
GPIO.setwarnings(False)
#Seleccionar el modo del GPIO
GPIO.setmode(GPIO.BCM)
#Settear el PIN del buzzer e inicializar
buzzer=26
GPIO.setup(buzzer,GPIO.OUT)

#Inicializando los LED's apagados
verde.off()
amarillo.off()

def check_in():
    #Medir la distancia
    try:
        while True:
            distance = sensor.distance * 100
            #Si la distancia es menor a 7 prender el foco verde
            if distance < 10:
                amarillo.off()
                verde.on()
                #Tomar la hora en la que acerco la mano e imprimirlo
                checkin = datetime.now()
                print("El sensor recibio el check-in de la mano... a las:", checkin)
                GPIO.output(buzzer,GPIO.LOW)
                verde.off()
                break
                        
            #Si la distancia es mayor a 10, encender el foco amarillo
            elif distance > 10:
                amarillo.on()
                verde.off()
                GPIO.output(buzzer,GPIO.HIGH)
                
            #Medir la distancia cada medio segundo
            time.sleep(1)
    except KeyboardInterrupt:
        print("Deteniendo...")