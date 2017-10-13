class DatabaseObject(object):
    def __init__(self, attrs, database_interface, on_chain=True):
        self.on_chain = on_chain
        self.attrs = attrs

        self.dbi = database_interface

        self.txid = None
        self.object_id = None

    def add_object(self, signer):
        self.txid = self.dbi.create_asset(self.attrs, signer)
        self.object_id = self.txid

        if not self.txid:
            raise Exception("Object creation unsuccessful")

        return self.txid

    def send_object(self, signer, recipient):
        if not self.txid:
            raise Exception("Object does not exist; cannot be send")

        self.txid = self.dbi.send_asset(self.txid, signer, recipient)

        return self.txid


class DatabaseToken():
    def __init__(self, attrs, database_interface, amount, on_chain=True):
        self.on_chain = on_chain
        self.attrs = attrs

        self.dbi = database_interface

        self.txid = None
        self.object_id = None
        self._amount = amount

    def send_object(self, signer, recipient, amount=0):
        if not self.txid:
            raise Exception("Object does not exist; cannot be send")

        self.txid = self.dbi.send_token(self.txid, signer, recipient, amount=amount)

        return self.txid

    def add_object(self, signer, recipient):
        self.txid = self.dbi.create_token(self.attrs, signer, recipient, self._amount)
        self.object_id = self.txid

        if not self.txid:
            raise Exception("Object creation unsuccessful")

        return self.txid
