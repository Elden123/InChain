from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

alice = generate_keypair()

tokens = {}
tokens['app_id'] = 'c3080fbc'
tokens['app_key'] = 'cdf98e4878062f34c2da1b94fab0b009'
bdb = BigchainDB('http://35.196.237.62:9984', headers=tokens)

bicycle_asset = {
    'data': {
        'bicycle': {
            'serial_number': 'asdfasdfasdf',
            'manufacturer': 'bkfab'
        },
    },
}

prepared_creation_tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    asset=bicycle_asset,
)

fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx,
    private_keys=alice.private_key
)

sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)


print()

print(bdb.assets.get(search='bicycle'))
