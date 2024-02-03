#Modelo base de Health-In-Motion
from gpiozero import LED, DistanceSensor
from datetime import datetime
import time

#Sensores base con 3 LED y el sensor de proximidad
sensor = DistanceSensor(echo = 14, trigger = 15)
verde = LED(13)
amarillo = LED(19)

#Inicializando los LED's apagados
verde.off()
amarillo.off()

#Medir la distancia
while True:
    distance = sensor.distance * 100
    print ("Distancia: ", distance)
    #Si la distancia es menor a 7 prender el foco verde
    if distance < 7:
        amarillo.off()
        verde.on()
        checkin = datetime.now()
        print("El sensor recibio el check-in de la mano... a las:", checkin)
                
    #Si la distancia es mayor a 7, encender el foco amarillo
    elif distance > 7:
        amarillo.on()
        verde.off()
        
    #Medir la distancia cada medio segundo
    time.sleep(0.5)