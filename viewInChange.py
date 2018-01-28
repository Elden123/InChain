from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
import csv

def viewEntry(name, key):

    parent = generate_keypair()

    tokens = {}
    tokens['app_id'] = 'c3080fbc'
    tokens['app_key'] = 'cdf98e4878062f34c2da1b94fab0b009'
    bdb = BigchainDB('https://test.bigchaindb.com', headers=tokens)
    number = key
    currentNode = str(number)
    nextNode = ""
    search = str(number)

    print(bdb.assets.get(search="Hey"))

    while bdb.assets.get(search=str(number)) != []:
        print("Current Node: " + currentNode)
        print(bdb.assets.get(search=str(number)))
        currentNode = bdb.assets.get(search=str(number))[0]['data']['link']['Next']
        number += 1

    nextNode = str(int(currentNode) + 1)
    print(bdb.assets.get(search=str(currentNode)))


viewEntry("Donald", 3336534)
#addUser("Eric", 3576895)
#addEntry("Zak", 1785043)
#addEntry("Nolan", 2302832)
