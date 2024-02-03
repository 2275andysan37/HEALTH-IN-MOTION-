#Modelo base de Health-In-Motion
from gpiozero import LED, DistanceSensor
import time

sensor = DistanceSensor(echo = 14, trigger = 15)
verde = LED(13)
amarillo = LED(19)
rojo = LED(26)
verde.off()
amarillo.off()
rojo.off()
while True:
    distance = sensor.distance * 100
    print ("Distancia: ", distance)
    
    if distance < 20:
        amarillo.off()
        verde.off()
        rojo.on()
    
    elif distance > 80:
        amarillo.off()
        rojo.off()
        verde.on()
        
    elif distance > 20 and distance < 80:
        verde.off()
        rojo.off()
        amarillo.on()
        
    time.sleep(0.5)