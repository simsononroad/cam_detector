import time
from datetime import datetime
from os import system as cmd

now = datetime.now()

def light_dark():
    """acth = time.localtime()[3]
    actm = time.localtime()[4]
    act = f"{acth}:{actm}"""
    act = 655
    napkelte = 656
    napnyugta = 1802


    if act >= napnyugta:
        print("Sötét van")
    elif act <= napnyugta:
        print("világos van")
    elif act >= napkelte:
        print("világos van")
    elif act <= napkelte:
        print("Sötét van")


def nowtime():
    ido = 0
    for i in range(60):
        ido += 1
        nowm = now.minute + ido 
    print(f"Time: {now.hour}:{nowm}:{now.second}")


def tryExcept():
        try:
            print("tes")
            time.sleep(10)
        except KeyboardInterrupt:
            down_counter = 3
            cmd("clear")
            for i in range(3, 0, -1):
                time.sleep(1)
                print(f"A program {i} másodperc múlva le fog állni")

if __name__ == "__main__":
    tryExcept()