from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    f = open("game.txt","r")
    return f.read()
