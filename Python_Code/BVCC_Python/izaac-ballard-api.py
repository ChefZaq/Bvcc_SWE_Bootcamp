import requests
import json
'''
API interaction 
Using http://jsonplaceholder.typicode.com, write a script to 
get the 200 most recent TODOs, 
create a TODO, and 
delete a TODO given an ID. 
First you need run “pip install request” if not already installed
Then “import request”
Name the file firstname-lastname-api.py
Enter a choice to do the get,create, or delete action 
'''

responseGet = requests.get('https://jsonplaceholder.typicode.com/todos').json()

for dictBlock in responseGet:  
    print(dictBlock)
print()

new_entry = {
    "userId": 11,
    "id": 201,
    "title": "the land before time",
    "completed" : True
}

responsePost = requests.post('https://jsonplaceholder.typicode.com/todos', data = new_entry)
print(responsePost)
print("Status Code" ,responsePost.status_code ,": A New Item Has Been Added")

new_entry_del = {
    "userId": 1,
    "id": 2,
    "title": 'quis ut nam facilis et officia qui',
    "completed" : False
}

responseDel  =  requests.delete('https://jsonplaceholder.typicode.com/todos', data = new_entry_del)
print(responseDel)
print("Status Code" ,responseDel.status_code , ": Our Item Has Been Deleted")