from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

def addEntry(name, key):

    parent = generate_keypair()

    tokens = {}
    bdb = BigchainDB('http://35.196.237.62:9984/', headers=tokens)#localhost:9984

    number = key
    currentNode = str(number)
    nextNode = ""
    search = str(number)

    while bdb.assets.get(search=str(number)) != []:
        print("Current Node: " + currentNode)
        currentNode = bdb.assets.get(search=str(number))[0]['data']['link']['Next']
        number += 1

    nextNode = str(int(currentNode) + 1)

    bicycle_asset = {
        'data': {
            'info': {
                'Description': 'You are sick.',
                'Doctor Name': 'Dr. John',
                'Patient Name': name,
                'Patient Phone Number': '1234567'
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

print()
#addEntry("Zak", 1785043)
#addEntry("Nolan", 2302832)
