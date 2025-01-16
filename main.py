from gtts import gTTS
import random

def speech(text, lang='en'):
    tts = gTTS(text, lang=lang)
    tts.save(f'Pyaudios/audio_{random.randint(0, 999999)}.mp3')

def get_language_input(languages):
    language = input("Enter the language of the text you are going to enter: ").lower()
    if language not in languages:
        print('The language you entered is not supported!')
        return None
    return language

def get_text_input():
    text = input("Enter the text (one paragraph only, no line breaks): ").strip()
    if text.count('\n') >= 1:
        print('Error: Enter one paragraph only.')
        return None
    return text

def main():
    languages = {
        "afrikaans": "af", "arabic": "ar", "bengali": "bn", "bosnian": "bs", "catalan": "ca",
        "czech": "cs", "danish": "da", "dutch": "nl", "english": "en", "filipino": "fil",
        "finnish": "fi", "french": "fr", "german": "de", "greek": "el", "gujarati": "gu",
        "hebrew": "he", "hindi": "hi", "hungarian": "hu", "icelandic": "is", "indonesian": "id",
        "italian": "it", "japanese": "ja", "javanese": "jw", "kannada": "kn", "khmer": "km",
        "korean": "ko", "latin": "la", "latvian": "lv", "macedonian": "mk", "malayalam": "ml",
        "marathi": "mr", "nepali": "ne", "norwegian": "no", "polish": "pl", "portuguese": "pt",
        "romanian": "ro", "russian": "ru", "serbian": "sr", "sinhala": "si", "slovak": "sk",
        "spanish": "es", "sundanese": "su", "swahili": "sw", "swedish": "sv", "tamil": "ta",
        "telugu": "te", "thai": "th", "turkish": "tr", "ukrainian": "uk", "urdu": "ur",
        "vietnamese": "vi", "welsh": "cy", "mandarin chinese": "zh-CN"
    }

    print('Welcome to Py text to speech converter...')
    language = get_language_input(languages)
    if language:
        text = get_text_input()
        if text:
            try:
                speech(text, lang=languages[language])
                print('File has been saved!!!')
            except Exception as e:
                print("Some error occurred!")
                print(f"Error details: {e}")
        else:
            print("Please enter valid text.")
    else:
        print("Please enter a valid language.")

if __name__ == "__main__":
    main()
