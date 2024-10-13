import time


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

if __name__ == "__main__":
    light_dark()