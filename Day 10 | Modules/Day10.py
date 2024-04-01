import speech_recognition as sr
import webbrowser
import pyautogui
import random
import time
recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio) 
        print(text)
        return text.lower()

MyFavMusic = ["Soothing Hindi","Hindi Songs", "Sonu Nigam","Arijit Singh"]
while True:    

    s = listen()

    if s in "good bye":
        print(text)
        print("Bye By Fun")
        break

    elif s in "hello" :
        print("Hello")
        break


    elif s in "open a website":
        print("Done")
        url = "https://www."+listen()+".com"
        webbrowser.open(url)

    elif s in "search on google":
        print("Done")
        url = "https://www.google.com/search?q="+listen()
        webbrowser.open(url)

    elif s in "play music":
        Cat = random.choice(MyFavMusic)
        url = "https://www.youtube.com/results?search_query="+Cat
        webbrowser.open(url)
        time.sleep(2)
        pyautogui.moveTo(320,300)
        time.sleep(1)
        pyautogui.click()
        



    
    else:
        print(text)
        print("I don't understand")