from bigchain_interface.bigchain_interface import BigchainInterface
from objects.database_object import DatabaseObject
from constants.constants import *
from bigchaindb_driver.crypto import generate_keypair


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
