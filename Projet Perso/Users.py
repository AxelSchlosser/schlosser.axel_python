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
                while i < 6:
                    #resp = json.loads(requests.get("https://www.netflix.com/api/shakti/v235006dc/viewingactivity?pg=" + str(i) + "&pgSize=20&guid=" + userID).content)
                    url = "https://www.netflix.com/api/shakti/v235006dc/viewingactivity?pg=" + str(i) + "&pgSize=20&guid=" + userID + "&_=1620226036865&authURL=1620205575102.zIvYfarf%2F0OaEesF85FD%2BIFFgsc%3D"
                    resp = requests.get(url)
                    print(url)
                    print(resp)
                    i+=1
    
    
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