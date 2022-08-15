import requests
import random
import colorama
import time

http = httpx.Client()

if (choice == "c"):
    i = int(input("How much char names you want to check: "))
delay = float(input("How much seconds you want to wait between requests: "))

    resp = http.get(f"https://github.com/{name}")

def checkchar():
    name = ""
    for x in range(i):
        name += random.choice("abcdefghijklmnopqrstuvwxyz1234567890")
    r = requests.get(f"https://github.com/{name}")
    if (r.status_code == 404):
        print(colorama.Fore.GREEN + f"{name} is available!")
        f.write(f"{name}\n")
    elif (r.status_code == 200):
        print(colorama.Fore.RED + f"{name} is not available!")
    elif (r.status_code == 429):
        print(colorama.Fore.RED + f"Getting rate limited, sleeping for 1s.")
        time.sleep(1)

def checkword():
    name = ""
    name = http.get("https://random-word-api.herokuapp.com/word").json()[0]
        print(colorama.Fore.GREEN + f"{name} is available!")
        f.write(f"{name}\n")
    elif (r.status_code == 200):
        print(colorama.Fore.RED + f"{name} is not available!")
    elif (r.status_code == 429):
        print(colorama.Fore.RED + f"Getting rate limited, sleeping for 1s.")
        time.sleep(1)     


while True:
    if (choice == "c"):
        checkchar()
    elif (choice == "w"):
        checkword()    
    time.sleep(delay)
