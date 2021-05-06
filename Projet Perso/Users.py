import json
import requests

class Users():    
    
    def __init__(self):
        pass
    
    def getStats(self, userID:str):
        with open('users.json', "r") as jsonFile:
            jsonData = json.load(jsonFile)
        for user in jsonData['users']:
            if user["userID"] != userID:
                pass
            else:
                i = 1
    
    
    def getUserName(self):
        with open('users.json', "r") as jsonFile:
            jsonData = json.load(jsonFile)
        for user in jsonData['users']:
            print(user["userName"])
            
    def getUserID(self):
        with open('users.json', "r") as jsonFile:
            jsonData = json.load(jsonFile)
        for user in jsonData['users']:
            print(user["userName"])