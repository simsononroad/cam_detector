import time
from datetime import datetime

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
    print(f"Time: {now.hour}:{now.minute + 1}:{now.second}")

if __name__ == "__main__":
    nowtime()