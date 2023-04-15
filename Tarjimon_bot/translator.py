from googletrans import Translator

def translator(message, lang1 = "uz", lang2 = "en"):
    translator = Translator()
    
    return translator.translate(message, src = lang1, dest = lang2).text

if __name__ == "__main__":
    print(translator("olma"))