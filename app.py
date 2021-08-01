from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <h1>So far 0!</h1>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)