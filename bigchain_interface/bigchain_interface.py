from bigchaindb_driver import BigchainDB


class BigchainInterface:
    def __init__(self, url, port):
        self.bdb = BigchainDB(url + ":" + port)

    def prepare_asset(self, operation, signers, asset):
        # Prepare asset data
        return self.bdb.transactions.prepare(
            operation=operation,
            signers=signers,
            asset=asset)

    def create_asset(self, prepared_data, private_key):

        print(prepared_data)

        # Sign transactions
        signed_tx = self.bdb.transactions.fulfill(prepared_data, private_key)

        # Send transaction
        send_tx = self.bdb.transactions.send(signed_tx)

        # Verify and return txid if succesful
        if send_tx == signed_tx:
            return signed_tx["id"]
        else:
            return False

    def check_transaction(self, txid):
        try:
            status = self.bdb.transactions.status(txid)
            return status
        except:
            return None

    def get_transaction(self, txid):
        return self.bdb.transactions.retrieve(txid)
