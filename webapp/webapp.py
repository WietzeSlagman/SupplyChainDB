from flask import *
from bigchain_interface.bigchain_interface import BigchainInterface
from constants.constants import *
import json

app = Flask(__name__)
app.config['DEBUG'] = True

db_interface = BigchainInterface(bdb_root_url, bdb_root_port)


@app.route("/")
def main():
    app.logger.debug('Loading %s' % (url_for('main')))

    return render_template("index.html")

@app.route("/get")
def get():
    app.logger.debug("You have arrived at " + url_for("get"))
    _id = request.args.get("id", None)
    _object = db_interface.get_transaction(_id)

    # Return the correct json file of the id
    if _object:
        return jsonify(_object)
    else:
        return jsonify({'result': 'Error'})


@app.route("/query")
def query():
    app.logger.debug("You have arrived at " + url_for("query"))
    query = request.args.get("q", None)
    _object = db_interface.query(query)

    # Return the correct json file of the id
    if _object:
        return jsonify(_object)
    else:
        return jsonify({'result': 'Error'})




if __name__ == "__main__":
    app.run()