from bigchaindb_driver import BigchainDB


class BigchainInterface:
    def __init__(self, url, port):
        self.bdb = BigchainDB(url + ":" + port)

    def create_asset(self, data, keypair):
        # Sign transactions

        pa = self._prepare_asset("CREATE", signers=keypair["public"], asset=data)
        signed_tx = self.bdb.transactions.fulfill(pa, keypair["private"])

        # Send transaction
        send_tx = self.bdb.transactions.send(signed_tx)

        # Verify and return txid if successful
        if send_tx == signed_tx:
            return signed_tx["id"]
        else:
            return False

    def check_transaction(self, txid):
        try:
            return self.bdb.transactions.status(txid)
        except:
            return None

    def get_transaction(self, txid):
        return self.bdb.transactions.retrieve(txid)

    def query(self, search, limit=None):
        return self.bdb.assets.get(search=search, limit=limit)

    def _prepare_asset(self, operation, **kwargs):
        # Prepare asset data
        return self.bdb.transactions.prepare(
            operation=operation,
            **kwargs)
