# realTimeTranslator

import openai

import pyttsx3
import speech_recognition as sr


openai.api_key = "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"





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



        INPUT = recordText()

        PROMPT = f"""

        You are a AI Therapist named Sukha, which meaning contentment and peace in Sanskrit. Your job is to speak as if you are a therapist to the user. The user statement is delimited by triple back ticks. Keep your response under 30 words. 

        User Statement: ```{INPUT}```

        """

        OUTPUT = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": PROMPT}]
        )

        AI_TEXT = OUTPUT.choices[0].message["content"]


        ENGINE = pyttsx3.init()
        ENGINE.say(AI_TEXT)
        ENGINE.runAndWait()















