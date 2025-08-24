import pyttsx3
import speech_recognition as sr
import

# Установите ваш API-ключ OpenAI
openai.api_key = "sk-wbWFGiEKeI9SzLoRqR8ClFHPWIWhKkw4"


def initialize_speaker():
    engine = pyttsx3.init()
    engine.setProperty('voice', 'ru')  # Установка русского голоса
    return engine


def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='ru-RU')
            print(f"Вы сказали: {command}")
            return command
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
            return ""
        except sr.RequestError:
            print("Ошибка сервиса распознавания речи")
            return ""


def chat_with_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']


def main():
    engine = initialize_speaker()
    speak(engine, "Привет! Я ваш умный голосовой помощник.")

    while True:
        command = listen().lower()
        if 'стоп' in command or 'выход' in command:
            speak(engine, "До свидания!")
            break
        elif 'как дела' in command:
            speak(engine, "У меня всё хорошо, спасибо!")
        elif 'что ты можешь' in command:
            speak(engine, "Я могу отвечать на вопросы и выполнять команды.")
        else:
            answer = chat_with_openai(command)
            speak(engine, answer)


if __name__ == "__main__":
    main()