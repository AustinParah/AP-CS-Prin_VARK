import requests

url ="https://random-word-api.herokuapp.com/word"
params = {'length': str(input('whats the length of the word boss? '))}

response = requests.get(url, params)


if(response.status_code != 200):
    print('unnable to pull from API -- using offline list')

wordJSON = response.json()
print(wordJSON[0])


