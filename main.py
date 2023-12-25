import openai
import pyttsx3
import speech_recognition as sr

from api_key import KEY


openai.api_key = KEY

RECOGNIZER = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                RECOGNIZER.adjust_for_ambient_noise(source2, duration=0.2)
                audio = RECOGNIZER.listen(source2)
                text = RECOGNIZER.recognize_google(audio)
                return text
        except sr.RequestError as e:
            print("Could not require results: {}".format(e))
        except sr.UnknownValueError:
            print("Unknown Value Error")
    return

def ai_therapist():
    input_text = record_text()
    prompt = f"""
    You are an AI therapist named Sukha, which means contentment and peace in Sanskrit. Your job is to speak as if you are a therapist to the user. The user statement is delimited by triple back ticks. Keep your response under 30 words.

    User Statement: ```{input_text}```
    """

    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    ai_text = output.choices[0].message["content"]

    engine = pyttsx3.init()
    engine.say(ai_text)
    engine.runAndWait()

def start_therapy():
    ai_therapist()

# Create GUI
"""root = tk.Tk()
root.title("AI Therapist")

start_button = tk.Button(root, text="Start Therapy", command=start_therapy)
start_button.pack()

root.mainloop()"""