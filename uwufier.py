#Imports
import time
import random

#The Intro or something
print("Made by Optimal7")
time.sleep(1)
print("Github Repo: https://github.com/Optimal7/uwufier")
time.sleep(1)
print("Note: This is made as a joke, so uh enjoy I guess.")
print("-------------------------------")
time.sleep(1)

#Loop so the program dose not stop but it goes on until you stop it.
while True:
    #Gets the text to uwufy
    print("What wouwd you wike to uwufy?")
    uwu = input("> ")

    #If there is no text (Not the best way to do it, don't know how to do it properly)
    if len(uwu) == 0:
        print("You nyeed to input text.")
        print("-------------------------------")
        time.sleep(2)

    else:
        #Replaces the stuff (uwufies the text given)
        uwu = uwu.replace('L', 'W')
        uwu = uwu.replace('R', 'W')
        uwu = uwu.replace('l', 'w')
        uwu = uwu.replace('r', 'w')
        uwu = uwu.replace("no", "nyo")
        uwu = uwu.replace("mo", "myo")
        uwu = uwu.replace("No", "Nyo")
        uwu = uwu.replace("Mo", "Myo")
        uwu = uwu.replace("na", "nya")
        uwu = uwu.replace("ni", "nyi")
        uwu = uwu.replace("nu", "nyu")
        uwu = uwu.replace("ne", "nye")
        uwu = uwu.replace("anye", "ane")
        uwu = uwu.replace("inye", "ine")
        uwu = uwu.replace("onye", "one")
        uwu = uwu.replace("unye", "une")

        #Random Emojis in messages
        emojis = ['(. ❛ ᴗ ❛.)', '(◕ᴗ◕✿)', '( ꈍᴗꈍ)', '(≧▽≦)', '(✿^‿^)', '(◠‿・)—☆', '>///<', '^v^', 'OwO', 'UwU', '^w^', '-w-']
        #emojis = random.choice(emojis)

        #If the message is more than 6 characters it will add a emoji from the "emojis" list.
        if len(uwu) > 6:
            emojis = random.choice(emojis)
        else:
            emojis = ""

        #Prints the UwUfied text
        print(uwu, emojis)
        print("-------------------------------")

        #Let's the code stop for 2 seconds and starts again.
        time.sleep(2)
