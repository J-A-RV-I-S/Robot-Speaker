import pyttsx3 # pyttsx3 is a library that converts text into speech.

if __name__ == "__main__":

    print("Welcome to RoboSpeaker, created by Jarvis")
    
    engine = pyttsx3.init() # init() is a factory function to get a reference to pyttsx3.

    while True:
        enter = input("What would you like me to speech: ")

        if enter == "exit":

            engine.say("Goodbye Jarvis")
            # say() is a inbuilt function in the pyttsx3, where the systems speaks to user.
             
            engine.runAndWait()
            # runAndWait() is an inbuilt function in the pyttsx3. It starts speech synthesis engine and block application untill system has finished speaking.
            
            break

        engine.say(enter)
        engine.runAndWait()
