from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
import csv

def addEntry(name, key):

    parent = generate_keypair()

    tokens = {}

    bdb = BigchainDB('http://35.196.237.62:9984/')#localhost:9984
    number = int(key)
    currentNode = str(number)
    nextNode = ""
    search = str(number)
    print("number" + str(number))
    print(bdb.assets.get(search=str(number)))

    while bdb.assets.get(search=str(number)) != []:
        print("Current Node: " + currentNode)

        currentNode = bdb.assets.get(search=str(number))[0]['data']['link']['Current']
        print(bdb.assets.get(search=str(number)))
        number += 1

    nextNode = str(int(currentNode) + 1)

    bicycle_asset = {
        'data': {
            'info': {
                'Data': 'Things'
            },
            'link': {
                'Current': currentNode,
                'Next': nextNode
            }
        },
    }

    prepared_creation_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=parent.public_key,
        asset=bicycle_asset,
    )

    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx,
        private_keys=parent.private_key
    )

    sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)
    print(bdb.assets.get(search=str(currentNode)))

def addUser(name, key):
    with open('keys.csv', 'a') as csvfile:
        fieldnames = ['name', 'key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'name': name, 'key': str(key)})

def userExists(name):
     with open('keys.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if(row['name'] == name):
                return(True)
        return(False)

def getUserKey(name):
    with open('keys.csv') as csvfile:
       reader = csv.DictReader(csvfile, delimiter=',')
       for row in reader:
           if(row['name'] == name):
               return(row['key'])
       return(0)

def viewEntry(name, key):

    parent = generate_keypair()

    tokens = {}
    tokens['app_id'] = 'a27cee86'
    tokens['app_key'] = 'a8229efe79f615dc4b901120ffa2e366'
    bdb = BigchainDB('http://35.196.237.62:9984/', headers=tokens)#localhost:9984
    number = key
    currentNode = str(number)
    nextNode = ""
    search = str(number)

    print(bdb.assets.get(search=str(currentNode)))

    while bdb.assets.get(search=str(number)) != []:
        print("Current Node: " + currentNode)
        currentNode = bdb.assets.get(search=str(number))[0]['data']['link']['Next']
        number += 1


print()
#addUser("Jon", 76512354)
addEntry("Eric", getUserKey("Eric"))

#addEntry("D", 2630754, "ccccccc", "a", "a", "a", "a", "a", "a", "a", "a")
print()
print()
print()
#
