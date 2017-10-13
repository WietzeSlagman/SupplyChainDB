from bigchaindb_driver import BigchainDB
from bigchaindb import Bigchain


class BigchainInterface:
    def __init__(self, url, port):
        connection = url + ":" + port

        self.bdb = BigchainDB(connection)
        self.bigchain_core = Bigchain(connection=connection)

    def create_asset(self, data, signer):
        signer = self._transform_key_pair(signer)

        # Sign transactions
        pa = self._prepare_asset("CREATE", signers=signer["public"], asset=data)
        signed_tx = self.bdb.transactions.fulfill(pa, signer["private"])

        # Send transaction
        send_tx = self.bdb.transactions.send(signed_tx)

        return self._verify_tx(signed_tx, send_tx)

    def send_asset(self, txid, signer, recipient):
        signer = self._transform_key_pair(signer)
        recipient = self._transform_key_pair(recipient)

        prev_tx = self.get_transaction(txid)
        pa = self._create_transfer_input(prev_tx, recipient["public"])

        signed_tx = self.bdb.transactions.fulfill(
            pa, private_keys=signer["private"]
        )

        send_tx = self.bdb.transactions.send(signed_tx)

        return self._verify_tx(signed_tx, send_tx)

    def create_token(self, data, creator, recipient, amount):
        recipient = self._transform_key_pair(recipient)
        creator = self._transform_key_pair(creator)

        pa = self._prepare_asset("CREATE", signers=creator["public"],
                                 recipients=[([recipient["public"]], amount)], asset=data)

        signed_tx = self.bdb.transactions.fulfill(pa, creator["private"])

        send_tx = self.bdb.transactions.send(signed_tx)

        return self._verify_tx(signed_tx, send_tx)

    def send_token(self, txid, signer, recipients, amount):
        signer = self._transform_key_pair(signer)
        recipient = ([self._transform_key_pair(r)["public"] for r in recipients], amount)
        spend = len(recipient[0]) * amount

        prev_tx = self.get_transaction(txid)

        current = sum([int(x["amount"]) for x in prev_tx["outputs"]
                       if signer["public"] == x["condition"]["details"]["public_key"]])

        pa = self._create_transfer_input(prev_tx, [recipient, ([signer["public"]], current-spend)])

        signed_tx = self.bdb.transactions.fulfill(
            pa, private_keys=signer["private"]
        )

        send_tx = self.bdb.transactions.send(signed_tx)

        return self._verify_tx(signed_tx, send_tx)

    def check_transaction(self, txid):
        try:
            return self.bdb.transactions.status(txid)
        except Exception as e:
            print(e)
            return None

    def get_transaction(self, txid):
        return self.bdb.transactions.retrieve(txid)

    def query(self, search, limit=None):
        return self.bdb.assets.get(search=search, limit=limit)

    def get_owned_ids(self, public_key):
        return self.bigchain_core.get_outputs_filtered(public_key)

    def _create_transfer_input(self, prev_tx, recipients):
        transfer_asset = {"id": None}
        if prev_tx["operation"] == "CREATE":
            transfer_asset["id"] = prev_tx["id"]
        elif prev_tx["operation"] == "TRANSFER":
            transfer_asset["id"] = prev_tx['asset']['id']

        output_index = 0
        output = prev_tx['outputs'][output_index]

        transfer_input = {
            'fulfillment': output['condition']['details'],
            'fulfills': {
                'output_index': output_index,
                'transaction_id': prev_tx['id'],
            },
            'owners_before': output['public_keys']
        }

        return self._prepare_asset("TRANSFER", asset=transfer_asset, inputs=transfer_input, recipients=recipients)

    def _prepare_asset(self, operation, **kwargs):
        # Prepare asset data
        return self.bdb.transactions.prepare(
            operation=operation, **kwargs)

    @staticmethod
    def _transform_key_pair(key_pair):
        if type(key_pair) != dict:
            return {"public": key_pair.public_key, "private": key_pair.private_key}

        return key_pair

    @staticmethod
    def _verify_tx(signed_tx, send_tx):
        # Verify and return txid if successful
        if send_tx == signed_tx:
            return signed_tx["id"]
        else:
            return False
