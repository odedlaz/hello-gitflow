from flask import Flask
import werkzeug
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/say/<text>')
def say(text):
   return "you said: %s" % text

@app.route('/ip')
def ip():
   return requests.get("https://api.ipify.org")

if __name__ == '__main__':
    app.run(debug=True)
