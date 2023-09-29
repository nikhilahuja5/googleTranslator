import googletrans
import speech_recognition
import gtts 
import playsound

intput_lang = "hi"
output_lang= "fr"

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language=intput_lang)
    print(text)


translator = googletrans.Translator()
translation = translator.translate(text,dest=output_lang)
print(translation.text)
converted_voice = gtts.gTTS(translation.text,lang=output_lang)
converted_voice.save("voice.mp3")
playsound.playsound("voice.mp3")





