import os
import requests
import time

while True:

    os.system('cls' if os.name=='nt' else 'clear')

    print("!   Vanity WebHook tool   !")
    print("")
    print("")
    print("")
    print("(1)  Webhook Spammer       (2)  Webhook Checker       (3)  Credits")
    print("")
    print("(4)  Soon                  (5)  Soon                  (6)  Soon")
    print("")
    print("")
    print("")

    select = input("[+] Select an option: ")
    if select == "1":
        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!   Webhook Checker   !")
        print("")
        print("")
        print("")
        webhook_url = input("[+] Webhook url: ")

        while True:
            message = input("[+] Message to send: ")
            data = {
                "content": message
            }

            response = requests.post(webhook_url, json=data)

            print("")
            print("[+] Message send")
    if select == "2":
        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!   Webhook Checker   !")
        print("")
        print("")
        print("")
        webhook_url = input("[+] Webhook url: ")

        data = {
            "content": "```Your Webhook is working!```"
        }
        response = requests.post(webhook_url, json=data)

        print("")
        print("[+] Message send!")
        break
    if select == "3":
        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!    Credits    !")
        print("")
        print("")
        print("")
        print("[-]  Made by Blxdes 2#1985")
        print("")
        print("[-]  Join the Discord: https://discord.gg/TDNYaWvyfZ")
        print("")
        print("")
        print("(0)  Go back")
        print("")
        print("")
        select = input("[+] Select an option: ")
        if select == "0":
            continue
    if select == "0":
        continue

# Btw why are you looking at the code?