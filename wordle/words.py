import requests
import random
import json


url ="https://random-word-api.herokuapp.com/word"
params = {'length': str()}


def getWord():
    response = requests.get(url, params)

    if(response.status_code != 200):
        print('unnable to pull from API -- using offline list')
        return getOfflineWord()

    wordJSON = response.json()
    print(wordJSON[0])
    return wordJSON[0]

def RegenerateOfflineWordlist():
    params = {'length': '5', 'number': '40'}

    with open('offlineWords.json', 'w') as file:
        json.dump(requests.get(url, params).json(), file)

def getOfflineWord():
    with open('offlineWords.json') as wordsJSON:
        wordsList = json.load(wordsJSON)
    return wordsList[random.randrange(0,39)]

