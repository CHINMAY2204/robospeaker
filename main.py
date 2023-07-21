
import pyttsx3

if __name__ == '__main__':
    print("welcome to robospeaker 1.1 created by chinu")
    while True:
        x = input("Enter what do you want me to speak: ")
        if x == "q":
            break
        engine=pyttsx3.init()
        engine.say(x)
        engine.runAndWait()










