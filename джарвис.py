import pyttsx3
import speech_recognition as sr
import pyaudio
def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech")
        return ""
    except sr.RequestError as e:
        print(f"Error accessing the speech recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen().lower()

        if "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("You said: " + command)