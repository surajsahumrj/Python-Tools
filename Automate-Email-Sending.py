import smtplib
import speech_recognition as sr
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen to user's voice
def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        speak("Sorry, I didn't catch that.")
        return None

# Send Email
def send_email(to, content):
    # Replace these with your email credentials (use an app password for Gmail)
    sender_email = "youremail@gmail.com"
    sender_password = "yourapppassword"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, content)
    server.quit()

def main():
    speak("Who is the recipient?")
    to = get_audio()
    if to:
        # You can map names to emails or just use full email addresses
        emails = {
            "myself": "yourfriend@gmail.com"
        }
        to_email = emails.get(to.lower(), None)
        if not to_email:
            speak("Sorry, I don't have that contact.")
            return

        speak("What is the message?")
        content = get_audio()
        if content:
            send_email(to_email, content)
            speak("Email has been sent successfully!")
        else:
            speak("No message detected.")
    else:
        speak("No recipient detected.")

if __name__ == "__main__":
    main()
