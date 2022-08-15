import requests
import random
import colorama
import time

http = httpx.Client()
names_file = "names.txt"

def valid_name(name):
    """
    Returns True if the name is available, False otherwise. And "ratelimited" if the API is ratelimited.
    """

    resp = http.get(f"https://github.com/{name}")

    if resp.status_code == 404:
        return True
    elif resp.status_code == 200:
        return False
    elif resp.status_code == 429:
        return "ratelimited"
def add_name_to_file(name):
    with open(names_file, "a") as f:
        f.write(f"{name}\n")
    name = ""
    valid = valid_name(name)
    if valid:
        print(colorama.Fore.GREEN + f"{name} is available!")
        add_name_to_file(name)
    elif not valid:
        print(colorama.Fore.RED + f"{name} is not available!")
    elif valid.lower() == "ratelimited":
        print(colorama.Fore.RED + f"Getting rate limited, sleeping for 1s.")
        time.sleep(1)

def checkword():
    name = ""
    name = http.get("https://random-word-api.herokuapp.com/word").json()[0]
    valid = valid_name(name)
    if valid:
        print(colorama.Fore.GREEN + f"{name} is available!")
        add_name_to_file(name)
    elif not valid:
        print(colorama.Fore.RED + f"{name} is not available!")
    elif valid.lower() == "ratelimited":
        print(colorama.Fore.RED + f"Getting rate limited, sleeping for 1s.")
        time.sleep(1)     


while True:
    if (choice == "c"):
        checkchar()
    elif (choice == "w"):
        checkword()    
    time.sleep(delay)
