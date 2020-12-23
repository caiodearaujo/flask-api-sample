from uuid import uuid4
from flask import Flask, jsonify
from argparse import ArgumentParser
from user_resource import user_path

app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(user_path)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0')