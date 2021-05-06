import os
import sys
import json

from Users import Users
 
 
#Fichier de test 
def main():
    user = Users()
    user.getStats("4M4232SANZBXHNJ7FAAQUV6NY4")
    
if __name__ == '__main__':
    main()    