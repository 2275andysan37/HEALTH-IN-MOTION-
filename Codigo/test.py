#Modelo base de Health-In-Motion
from gpiozero import LED, DistanceSensor
import time

#Sensores base con 3 LED y el sensor de proximidad
sensor = DistanceSensor(echo = 14, trigger = 15)
verde = LED(13)
amarillo = LED(19)
rojo = LED(26)

#Inicializando los LED's apagados
verde.off()
amarillo.off()
rojo.off()

#Medir la distancia
while True:
    distance = sensor.distance * 100
    print ("Distancia: ", distance)
    #Si la distancia es menor a 20cm prender el foco rojo
    if distance < 20:
        amarillo.off()
        verde.off()
        rojo.on()
        
    #Si la distancia es mayor a 80, encender el foco verde
    elif distance > 80:
        amarillo.off()
        rojo.off()
        verde.on()
        
    #Si la distancia es mayor a 20cm y menos a 80cm, encender el foco amarillo
    elif distance > 20 and distance < 80:
        verde.off()
        rojo.off()
        amarillo.on()
        
    time.sleep(0.5)