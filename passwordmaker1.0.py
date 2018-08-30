#!/bin/usr/env python3
#Title : PasswordMaker
#Author: Phemt91
# ____  _                    _    ___  _
#|  _ \| |__   ___ _ __ ___ | |_ / _ \/ |
#| |_) | '_ \ / _ \ '_ ` _ \| __| (_) | |
#|  __/| | | |  __/ | | | | | |_ \__, | |
#|_|   |_| |_|\___|_| |_| |_|\__|  /_/|_|
#

import random, os


fullchar="""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
alphachar="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main():
    while True:
        global scelta

        print(""" ____  _                    _    ___  _
|  _ \| |__   ___ _ __ ___ | |_ / _ \/ |
| |_) | '_ \ / _ \ '_ ` _ \| __| (_) | |
|  __/| | | |  __/ | | | | | |_ \__, | |
|_|   |_| |_|\___|_| |_| |_|\__|  /_/|_|
                        PasswordMaker1.0        """)

        print("\nScegli il numeri di carattari")
        scelta=input("\n--> ")
        if scelta=="clean":
            pulisci()
        elif scelta=="stop":
            pulisci()
            break
        elif scelta.isalpha():
            print("Errore Tecnico, inserisci un numero")
        else:
            choicechar()
            password_10()


def choicechar():
    global chara
    choicech=input("\n\nInserisci che tipo di caratteri usare --> ")
    if choicech=="A":
        pulisci()
        print("## Scelto set di caratteri Alphanumerici ##")
        chara=alphachar
    else:
        pulisci()
        print("## Scelto set di caratteri FULL ##")
        chara=fullchar


def password_10():
    print("\n\n## password ##\n\n")
    global scelta
    print(scelta)
    password=("".join([random.choice(chara) for _ in range(int(scelta))]))
    print(password)
    print("""\n###///###\\\###\n\n""")


def pulisci():
    os.system("clear")

main()
