from flask import Flask
import werkzeug
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! 2'

if __name__ == '__main__':
    app.run(debug=True)
