class DatabaseObject(object):
    def __init__(self, attrs, database_interface, on_chain=True):
        self.on_chain = on_chain
        self.attrs = attrs

        self.dbi = database_interface

        self.txid = None

    def add_object(self, keypair):
        if type(keypair) != dict:
            keypair = {"public": keypair.public_key, "private": keypair.private_key}


        pa = self.dbi.prepare_asset("CREATE", keypair["public"], self.attrs)

        self.txid = self.dbi.create_asset(pa, keypair["private"])

        if not self.txid:
            print("Object creation unsuccessful")
            raise(Exception)

        return self.txid
