from bigchain_interface.bigchain_interface import BigchainInterface
from objects.database_object import DatabaseObject
from constants.constants import *
from bigchaindb_driver.crypto import generate_keypair
from time import sleep

db_interface = BigchainInterface(bdb_root_url, bdb_root_port)

bicycle_attrs = {
    'data': {
        'type': 'bicycle',
        'serial_number': 'abcd1234',
        'manufacturer': 'bkfab',
    }
}

bicycle = DatabaseObject(bicycle_attrs, db_interface)

bob = generate_keypair()
alice = generate_keypair()
richard = generate_keypair()

print("Public key Bob: \t%s" % bob.public_key)
print("Public key Alice: \t%s" % alice.public_key)
print("Public key Richard: %s" % richard.public_key)

print("-----------------------------------------------")

print("Object id: %s" % bicycle.add_object(bob))

print("First check transaction: \t%s" % db_interface.check_transaction(bicycle.txid))

sleep(2)

print("Second check transaction: \t%s" % db_interface.check_transaction(bicycle.txid))
print("Get transaction return: \t%s" % db_interface.get_transaction(bicycle.txid))
print("Query result: \t\t\t\t%s" % db_interface.query(bicycle.object_id))

print("-----------------------------------------------")

print("Object id: %s" % bicycle.send_object(bob, alice))

print("First send transaction: \t%s" % db_interface.check_transaction(bicycle.txid))

sleep(2)

print("Second send transaction: \t%s" % db_interface.check_transaction(bicycle.txid))
print("Get transaction return: \t%s" % db_interface.get_transaction(bicycle.txid))
print("Query result: \t\t\t\t%s" % db_interface.query(bicycle.object_id))

print("-----------------------------------------------")

print("Object id: %s" % bicycle.send_object(alice, richard))

print("First send transaction: \t%s" % db_interface.check_transaction(bicycle.txid))

sleep(2)

print("Second send transaction: \t%s" % db_interface.check_transaction(bicycle.txid))
print("Get transaction return: \t%s" % db_interface.get_transaction(bicycle.txid))
print("Query result: \t\t\t\t%s" % db_interface.query(bicycle.object_id))