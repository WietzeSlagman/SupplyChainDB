# SupplyChainDB
Implementation of supplychain using BigChainDB

---

Starting BigchainDb:

```bash
    docker pull bigchaindb/bigchaindb

    sudo bash bash/configure.sh
    sudo bash bash/start.sh

    python3 -m test.test_simple # Works if BigchainDb is correctly initialized 
```

---

Run webapp/webapp.py for Flask server.

The different pages are as follows:
- /get: GET method, takes "id" argument. Returns the database object with same id as JSON.
- /query: GET method, takes "q" argument. Returns the "q" query results from the database as JSON.
- /db_debug: GET method, takes "q" argument. Similiar to /query, only now shows results in HTML table usefull for quick database overview
- /create: POST method, requires a JSON file/object. Will create the object from the "data" key in the database with the signatures coming from the keypair. The JSON file needs contain a "data" key. If no keypair is given, or the values are empty, a new one is generated. An example JSON will be given below:

```json
{
    "data": {
        "type": "bicycle",
        "serial_number": "abcd1234",
        "manufacturer": "bkfab"
    },
    "keypair": {
        "private": "<PRIVATE_KEY>",
        "public": "<PUBLIC_KEY>"
        
    }
}
```
