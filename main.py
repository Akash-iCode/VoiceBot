import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)


conversation = ""
user_name = "Akash"
bot_name = "Jarvis"
engine.say(" Hello, I am Jarvis Your Personal AI Assistant " )
print("Hello, I am Jarvis Your Personal AI Assistant ")
while True:
    with mic as source:
        print("\nlistening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening.\n")
    
    try:
        user_input = r.recognize_google(audio)
        print("user input : " + user_input)
    except Exception as e :
        print(e)
        continue
    
    prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "
    
    conversation += prompt
    
    response = openai.Completion.create(engine='text-davinci-001', prompt=conversation, max_tokens=200)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
    
    conversation += response_str + "\n"
    print(response_str)
    
    engine.say(" Here's what I found  "+"  "+response_str)
    engine.runAndWait()










#pip install -r installScrepts.txt