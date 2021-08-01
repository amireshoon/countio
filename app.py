from flask import Flask, jsonify
from src.storage import ioStorage

app = Flask(__name__)
ls = ioStorage()

@app.route('/')
def index():
    
    return """
        <h1>So far 0!</h1>
    """

@app.route('/new/account')
def new_account():
    return jsonify(ls.store_account("test"))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)