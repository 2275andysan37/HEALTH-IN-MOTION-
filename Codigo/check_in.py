#Modelo base de Health-In-Motion
from gpiozero import LED, DistanceSensor
from datetime import datetime
import RPi.GPIO as GPIO
import time
import bd

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
GPIO.output(buzzer,GPIO.LOW)

def check_in():
    #Medir la distancia
    bucle = True
    while bucle:
        distance = sensor.distance * 100
        #Si la distancia es menor a 10 prender el foco verde
        if distance < 10:
            amarillo.off()
            verde.on()
            #Tomar la hora en la que acerco la mano e imprimirlo
            p = datetime.now()
            checkin = p.strftime('%Y-%m-%d %H:%M:%S')
            bd.grabar_datos(checkin)
            print("El sensor recibio el check-in de la mano... a las:", checkin)
            GPIO.output(buzzer,GPIO.LOW)
            verde.off()
            bucle = False
            break
                        
        #Si la distancia es mayor a 10, encender el foco amarillo
        elif distance > 10:
            amarillo.on()
            verde.off()
            GPIO.output(buzzer,GPIO.HIGH)
                
        #Medir la distancia cada segundo
        time.sleep(1)