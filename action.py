import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather


def Action(data):
    user_data = data.lower()

    if"what is your name" in user_data:
        text_to_speech.text_to_speeh("My name is virtual assistant")
        return"My name is virtual assitant"
    

    if"hello" in user_data or "hye" or "how are you" in user_data:
        text_to_speech.text_to_speeh("Hey, how can i help you")
        return" How can i help you"

    if"good morning" in user_data:
        text_to_speech.text_to_speeh("Good Morning sir")
        return" Good morning"      
    if"Time" in user_data:
        current_time=datetime.datetime.now()
        Time =(str)(current_time)+"Hour :",(str)(current_time.minute)+"Minute"
        text_to_speech.text_to_speeh(Time)
        return Time

    if"shutdown".lower() in user_data:
        text_to_speech.text_to_speeh("ok sir")
        return "ok sir"
    if"play music" in user_data:
        webbrowser.open("https://ganna.com/")
        text_to_speech.text_to_speeh("select your music")
        return "select your music"
    
    if"youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speeh("Youtube is ready ")
        return"Youtube is ready"
    
    if"google"in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speeh("Google ")
        return"Google"
    
    if"weather" in user_data:
        ans =weather.weather()
        text_to_speech.text_to_speeh(ans)
        return ans
    

    else:
        text_to_speech.text_to_speeh("Soory i didnt undertsand")    
        return "Sorry i didnt understand"