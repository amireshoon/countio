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

@app.route('/new/account')
def new_account():
    return jsonify(ls.store_account("test"))

@app.route('/remove/account')
def remove_account():
    return jsonify(ls.remove_account("test"))

@app.route('/count/+')
def increase_count():
    return jsonify(ls.increase_count("f8b9b1ba18"))

@app.route('/count/-')
def decrease_count():
    return jsonify(ls.decrease_count("f8b9b1ba18"))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)