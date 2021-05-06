import json
import requests
import pandas as pd
from pandas.io.json import json_normalize 

class Users():    
    
    def __init__(self):
        pass
    
    def getStats(self, userID:str):
        with open('users.json', "r") as jsonFile:
            jsonData = json.load(jsonFile)
        for user in jsonData['users']:
            if user["userID"]  != userID:
                
                #L'utilisateur n'est pas trouvé
                pass
            else:
                
                #On trouve l'utilisateur dans le JSON avec l'ID passé dans la fonction.
                #Problème de parsing du tableau
                #La rfonction splitData ne fonctionne pas je n'ai pas réussi à utiliser la fonction json_normalize de pandas.
                #On peut la mettre en commentaire pour accéder à la fonction de création du fichier excel
                with open('users.json', "r") as jsonFile:
                    parsedJSON = json.loads(jsonFile.read())
                    print(parsedJSON["users"])
                    splitData = pd.json_normalize(parsedJSON, record_path =user["userName"], 
                                                            meta =['title','videoTitle','movieID'])
                    print(splitData)
                    
                    # Création d'un document Excel regroupant toutes les statistiques pour chaque personne.
                    with pd.ExcelWriter(r'C:\Users\axel6\Documents\schlosser.axel_python\Projet Perso\Statistiques_Netflix.xls') as writer:
                        tableauJSON.to_excel(writer)
    
    
    #Getter
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