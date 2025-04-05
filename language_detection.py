from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

def detect_language(text):
    try:
        language = detect(text)
        return language
    except LangDetectException:
        return "Language could not be detected."

if __name__ == "__main__":
    text = input("Enter text to detect the language: ")

    detected_language = detect_language(text)
    
    print(f"Detected Language: {detected_language}")
