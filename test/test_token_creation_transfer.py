from bigchain_interface.bigchain_interface import BigchainInterface
from objects.database_object import DatabaseToken
from constants.constants import *
from bigchaindb_driver.crypto import generate_keypair
from time import sleep

db_interface = BigchainInterface(bdb_root_url, bdb_root_port)

token_attrs = {
    "data": {
        "token_for": {
            "bicycle": {
                "serial_number": "abc1234",
                "manufacturer": "bkfab"
            }

        }
    }
}

token = DatabaseToken(token_attrs, db_interface, 100)

bob = generate_keypair()
alice = generate_keypair()
richard = generate_keypair()

print("Public key Bob: \t%s" % bob.public_key)
print("Public key Alice: \t%s" % alice.public_key)
print("Public key Richard: %s" % richard.public_key)

print("-----------------------------------------------")

print("Object id: %s" % token.add_object(bob, bob))

print("First check transaction: \t%s" % db_interface.check_transaction(token.txid))

sleep(2)

print("Second check transaction: \t%s" % db_interface.check_transaction(token.txid))
print("Get transaction return: \t%s" % db_interface.get_transaction(token.txid))
print("Query result: \t\t\t\t%s" % db_interface.query(token.object_id))

print("-----------------------------------------------")

print("Object id: %s" % token.send_object(bob, [alice], amount=10))

print("First send transaction: \t%s" % db_interface.check_transaction(token.txid))

sleep(2)

print("Second send transaction: \t%s" % db_interface.check_transaction(token.txid))
print("Get transaction return: \t%s" % db_interface.get_transaction(token.txid))
print("Query result: \t\t\t\t%s" % db_interface.query(token.object_id))

print("-----------------------------------------------")

print("Object id: %s" % token.send_object(alice, [richard], amount=5))

print("First send transaction: \t%s" % db_interface.check_transaction(token.txid))

sleep(2)

print("Second send transaction: \t%s" % db_interface.check_transaction(token.txid))
print("Get transaction return: \t%s" % db_interface.get_transaction(token.txid))
print("Query result: \t\t\t\t%s" % db_interface.query(token.object_id))

print("-----------------------------------------------")
