class Database_object(object):
    def __init__(self, attrs, signer, database_interface, on_chain=True):
        self.on_chain = on_chain
        self.attrs = attrs

        self.dbi = database_interface
        self.signer = signer

    def add_object(self):
        pa = self.dbi.prepared_asset("CREATE", self.signer, self.attrs)

        if not create_asset(pa):
            print("Object creation unsuccesful")
            raise(Exception)
