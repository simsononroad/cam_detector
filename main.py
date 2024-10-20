import cv2
import requests
from time import sleep, time, ctime
from daniwled import wled as led
from os import system as cmd
from datetime import datetime

now = datetime.now()

# HOG alapú emberi alak detektor betöltése
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Webkamera megnyitása
cap = cv2.VideoCapture(0)

# Állapotváltozó, hogy csak egyszer írja ki a "szia" üzenetet
detected = False
led_on = False
when_turn_on = 0
when_stop_mp = 2
ido = 0
mekkora_az_eselye_h_ember = 1.6
mennyi_ido_mulva_alljon_le = 60


def stop():
    down_counter = when_stop_mp
    cmd("clear")
    for i in range(when_stop_mp, 0, -1):
        sleep(1)
        print(f"A program {i} másodperc múlva le fog állni")
        sleep(1)
        exit()


print("Az alkalmazást a ctrl+c segítségével tudod bezárni vagy az exit parancsal")
try:
    while True:
        # Kép beolvasása
        ret, frame = cap.read()
        if not ret:
            break

        # Kép konvertálása szürkeárnyalatúra
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Emberi alakok detektálása
        human_boxes, valoszinuseg = hog.detectMultiScale(gray_frame, winStride=(8, 8), padding=(16, 16), scale=1.05)

        # Kiírás az észlelt emberi alakok számáról
        detected = False

        #Ember detektálása ha 0.7nél nagyobb valószínűséggel ember

        for i in valoszinuseg:
            if i >= mekkora_az_eselye_h_ember:
                detected = True
                when_turn_on = time()
                cmd("clear")
                print(f"Ember érzékelve: {len(human_boxes)}, valószínüség: [{valoszinuseg}]. Ekkor: {ctime()}.")
                kilep = input("")
                if kilep == "exit":
                    stop()
                break

        
        # LED vezérlés az észlelt emberi alakok alapján
        if detected:
            if not led_on:
                led(255)
                led_on = True
            

        # Kép megjelenítése
        #cv2.imshow('Video', frame)

        #Csak akkor kapcsol ki a led ha 60 másodpercig nem érzékelt senkit
        if when_turn_on+mennyi_ido_mulva_alljon_le < time():
            led(10)
            led_on = False
            

        # Kilépés ha 'q'-t nyomunk
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    stop()

# Kamera és ablakok bezárása
cap.release()
cv2.destroyAllWindows()
