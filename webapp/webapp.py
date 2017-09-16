from flask import *
from flask_table import *
from bigchain_interface.bigchain_interface import BigchainInterface
from objects.database_object import DatabaseObject
from bigchaindb_driver.crypto import generate_keypair

from constants.constants import *

app = Flask(__name__)
app.config['DEBUG'] = True

db_interface = BigchainInterface(bdb_root_url, bdb_root_port)


@app.route("/")
def main():
    app.logger.debug('Loading %s' % (url_for('main')))

    return render_template("index.html")


@app.route("/test")
def test():
    app.logger.debug('Loading %s' % (url_for('test')))

    return render_template("test.html")


@app.route("/get", methods=["GET"])
def get():
    app.logger.debug("You have arrived at " + url_for("get"))
    _id = request.args.get("id", None)
    _object = db_interface.get_transaction(_id)

    # Return the correct json file of the id
    if _object:
        return jsonify(_object)
    else:
        return jsonify({'result': 'Error'})


@app.route("/query", methods=["GET"])
def query():
    app.logger.debug("You have arrived at " + url_for("query"))
    query = request.args.get("q", None)
    _object = db_interface.query(query)

    # Return the correct json file of the id
    if _object:
        return jsonify(_object)
    else:
        return jsonify({'result': 'Error'})


@app.route("/db_debug", methods=["GET"])
def db_debug():
    app.logger.debug("You have arrived at " + url_for("db_debug"))
    query = request.args.get("q", None)

    _object = db_interface.query(query)

    for x in _object:
        x["data"]["id"] = x["id"]

    data = [x["data"] for x in _object]

    columns = set(sum([list(x.keys()) for x in data], []))

    m_table = create_table("table")

    for c in columns:
        m_table = m_table.add_column(c, Col(c))

    return render_template("db_debug.html", table=m_table(data))


@app.route("/create", methods=["POST"])
def create():
    app.logger.debug("You have arrived at " + url_for("create"))

    if request.is_json:
        data = request.get_json(force=True)
        print("json: %s" % data)

        _object = DatabaseObject(data, db_interface)
        
        # TODO Remove this if not DEMO
        if not data["keypair"]:
            keypair = generate_keypair()
        # TODO Remove this if not DEMO
        elif not keypair["public"] or not keypair["private"]:
            keypair = data["keypair"]
            print("Non valid keychain; new one is created for DEMO")
        else:
            keypair = data["keypair"]

            keypair = generate_keypair()

        txid = _object.add_object(keypair)

        print("Object created: %s" % txid)

    return render_template('index.html')


if __name__ == "__main__":
    app.run()
