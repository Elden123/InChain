from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

#alice = generate_keypair()
#private key 7u4AMhnb4RDRZmsEmrVxo9R8Mdpd8qA8erGGC9yWtJq1
#public key 5JGVfHkmTdv8cdxbHtfqjsP35sn1uSXi8csFbi4n1SoM
public_keyA = '5JGVfHkmTdv8cdxbHtfqjsP35sn1uSXi8csFbi4n1SoM'
private_keyA = '7u4AMhnb4RDRZmsEmrVxo9R8Mdpd8qA8erGGC9yWtJq1'


tokens = {}
tokens['app_id'] = 'c3080fbc'
tokens['app_key'] = 'cdf98e4878062f34c2da1b94fab0b009'
bdb = BigchainDB('https://test.bigchaindb.com', headers=tokens)#localhost:9984

bicycle_asset = {
    'data': {
        'bicycle': {
            'serial_number': '4857dvjdhv7',
            'manufacturer': 'bkfab'
            'points to': 'as;dflkj'
            'points from': 'as;dlkf'
        },
    },
}

bicycle_asset_metadata = {
    'planet': 'earth'
}

prepared_creation_tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=public_keyA,
    asset=bicycle_asset,
    metadata=bicycle_asset_metadata
)

fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx,
    private_keys=private_keyA
)

sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)

print()
print(bdb.assets.get(search='4857dvjdhv7'))
#print(alice)
print()
