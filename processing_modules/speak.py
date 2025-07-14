import pyttsx3
 
# init function to get an engine instance for the speech synthesis 
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    # say method on the engine that passing input text to be spoken
    engine.say('Hello sir,how may I help you, sir.')
    # run and wait method, it processes the voice commands. 
    engine.runAndWait()