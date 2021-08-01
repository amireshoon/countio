from flask import Flask, jsonify
from src.storage import ioStorage

app = Flask(__name__)
ls = ioStorage()

@app.route('/')
def index():
    return ls.search_in_accounts('test')
        
    return """
        <h1>So far 0!</h1>
    """

@app.route('/new/account/<name>')
def new_account(name):
    return jsonify(ls.store_account(name))

@app.route('/remove/account/<name>')
def remove_account(name):
    return jsonify(ls.remove_account(name))

@app.route('/count/<hid>/+')
def increase_count(hid):
    return jsonify(ls.increase_count(hid))

@app.route('/count/<hid>/-')
def decrease_count(hid):
    return jsonify(ls.decrease_count(hid))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)