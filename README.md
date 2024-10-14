# Magyar
# Telepítés linuxon:
1. virtuális környezet létrehozása


`python3 -m venv myenv`


`source myenv/bin/activate`


2. OpenCV telepítése

   
`pip3 install opencv-python`


3. Mi a wled IP-ja?

Írd be a terminálba: `host [your wled domain]`



3. VSCode újraindítása


4. Megnézni hogy sikeresen letöltődött
```
python3
>>>import cv2
>>>print(cv2.__version__)
```


# English
# Install on linux:
1. Create a virtual enviroment


`python3 -m venv myenv`


`source myenv/bin/activate`


2. install OpenCV

   

`pip3 install opencv-python`

3. What is your wled ip

Write to your terminal: `host [your wled domain]`



4. Restart the VSCode


5. Check that it has been downloaded successfully
```
python3
>>>import cv2
>>>print(cv2.__version__)
```
