from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

bdb_root_url = 'https://test.bigchaindb.com'
bdb = BigchainDB(bdb_root_url)


doctor, patient = generate_keypair(), generate_keypair()

form1 = {
    'data': {
        'bicycle': {
            'serial_number': 'qwerty',
            'manufacturer': 'taco'
        },
    },
}

form2 = {
    'data': {
        'bicycle': {
            'serial_number': 'asdf',
            'manufacturer': 'burrito'
        },
    },
}

form1_creation_prep = bdb.transactions.prepare(
    operation='CREATE',
    signers=doctor.public_key,
    asset=form1,
)

form1_creation_fulfill = bdb.transactions.fulfill(
    form1_creation_prep,
    private_keys=alice.private_key
)

form1_creation_sent = bdb.transactions.send(form1_creation_fulfill)

print (alice)
print (bob)
