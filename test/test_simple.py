from bigchaindb_driver import BigchainDB

bdb_root_url = 'http://127.0.0.1:9984/'

bdb = BigchainDB(bdb_root_url)


bicycle = {
    'data': {
        'bicycle': {
            'serial_number': 'abcd1234',
            'manufacturer': 'bkfab',
        },
    },
}

from bigchaindb_driver.crypto import generate_keypair
alice, bob = generate_keypair(), generate_keypair()


prepared_creation_tx = bdb.transactions.prepare(
   operation='CREATE',
   signers=alice.public_key,
   asset=bicycle,
)

print(prepared_creation_tx)


fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx, private_keys=alice.private_key)

print(fulfilled_creation_tx)

sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)


if sent_creation_tx == fulfilled_creation_tx:
    print("\n\nShit works, bro")