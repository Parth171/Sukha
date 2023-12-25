import speech_recognition as sr
import pyttsx3
import pyaudio

# Initialize Recognizer
RECOGNIZER = sr.Recognizer()


def recordText():

    while True:
        try:
            with sr.Microphone() as source2:
                RECOGNIZER.adjust_for_ambient_noise(source2, duration=0.2)

                AUDIO = RECOGNIZER.listen(source2)

                TEXT = RECOGNIZER.recognize_google(AUDIO)

                return TEXT

        except sr.RequestError as e:
            print("Could not require results;".format(e))

        except sr.UnknownValueError:
            print("Unknown Value Error")

    return


if __name__ == "__main__":

    while True:

        print("listening...")

        text = recordText()

        print(text)