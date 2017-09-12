from flask import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def main():
    app.logger.debug('Loading %s' % (url_for('main')))


    return render_template("index.html")


if __name__ == "__main__":
    app.run()