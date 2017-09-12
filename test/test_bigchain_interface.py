from bigchain_interface.bigchain_interface import BigchainInterface
from objects.database_object import DatabaseObject
from constants.constants import *
from bigchaindb_driver.crypto import generate_keypair
from time import sleep

db_interface = BigchainInterface(bdb_root_url, bdb_root_port)

bicycle_attrs = {
    'data': {
        'bicycle': {
            'serial_number': 'abcd1234',
            'manufacturer': 'bkfab',
        },
    },
}

bicycle = DatabaseObject(bicycle_attrs, db_interface)

print("Id: %s" % bicycle.add_object(generate_keypair()))


print("First check transaction: %s" % db_interface.check_transaction(bicycle.txid))

sleep(2)

print("Second check transaction: %s" % db_interface.check_transaction(bicycle.txid))
print("Get transaction return: %s" % db_interface.get_transaction(bicycle.txid))
