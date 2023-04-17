import requests

API_key = "97f47aac5aa75bb5c571566057077647"
API_ID = 'f5694067'
language = 'en-gb'

def getDefination(word_ID):
    url = f"https://od-api.oxforddictionaries.com:443/api/v2/entries/{language}/{word_ID}"
    respons = requests.get(url, headers = {'app_id': API_ID, 'app_key': API_key})
    respons = respons.json()
    # print(respons)
    
    if 'error' in respons.keys():
        return f"{word_ID} wasn't found"
    
    definitions = f"🔍 definition of The {word_ID}\n"
    for lexicalEntries in respons['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:#[0]['definitions']
        definitions += f"💡 {lexicalEntries['definitions'][0]}\n"
    
    if respons['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        return definitions+'\n\n'+respons['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    else:
        return definitions


if __name__ == '__main__':
    # from pprint import pprint
    # print(getDefination('python'))
    
    
    import tempfile
    from pydub import AudioSegment
    from urllib.request import urlopen

    data = urlopen('https://audio.oxforddictionaries.com/en/mp3/python_1_gb_2.mp3').read()
    print(data)
    # f = tempfile.NamedTemporaryFile(delete=False)
    # f.write(data)
    # AudioSegment.from_mp3(f.name).export('result.ogg', format='ogg')
    # f.close()
