import cv2
import requests
from time import sleep, time, ctime
from daniwled import wled as led

# HOG alapú emberi alak detektor betöltése
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Webkamera megnyitása
cap = cv2.VideoCapture(0)

# Állapotváltozó, hogy csak egyszer írja ki a "szia" üzenetet
detected = False
led_on = False
when_turn_on = 0
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
        if i >= 0.7:
            detected = True
            when_turn_on = time()
            print(f"Ember érzékelve: {len(human_boxes)} [{valoszinuseg}]")
            break

    
    # LED vezérlés az észlelt emberi alakok alapján
    if detected:
        if not led_on:
            led(255)
            led_on = True


    # Ha talál emberi alakot, keretezd be
    if detected:
        for (x, y, w, h) in human_boxes:
            # Emberi alak keretezése
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        

    # Kép megjelenítése
    cv2.imshow('Video', frame)

    #Csak akkor kapcsol ki a led ha 60 másodpercig nem érzékelt senkit
    if when_turn_on+60 < time():
        led(10)
        led_on = False
        

    # Kilépés ha 'q'-t nyomunk
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera és ablakok bezárása
cap.release()
cv2.destroyAllWindows()
