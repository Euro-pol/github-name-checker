import httpx
import random
import colorama
import time

http = httpx.Client()
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
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
def check_char_name(length_of_name):
    name = ""
    for x in range(length_of_name):
        name += random.choice(alphabet)
    valid = valid_name(name)
    if valid:
        print(colorama.Fore.GREEN + f"{name} is available!")
        add_name_to_file(name)
    elif not valid:
        print(colorama.Fore.RED + f"{name} is not available!")
    elif valid.lower() == "ratelimited":
        print(colorama.Fore.RED + f"Getting rate limited, sleeping for 1s.")
        time.sleep(1)

def check_word_name():
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

    amount_of_names = int(input("How many names do you want to check (-1 for no limit)? "))
    if (choice == "c"):
        length_of_char_names = int(input("How long do you want the char names to be: "))

    count = 0
while True:
        if amount_of_names != -1:
            if count == amount_of_names:
                break
        if choice == "c":
            check_char_name(length_of_char_names)
        elif choice == "w":
            check_word_name()  
        count += 1
    time.sleep(delay)
