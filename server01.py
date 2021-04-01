from flask import Flask
from flask import jsonify
import json


app = Flask(__name__)

@app.route('/')
def index():
    return "helo, flask"
    
@app.route('/quotes')
def quotes():
    manipulador = open('quotes.json','r')
    mp = json.load(manipulador)
    return jsonify(mp)
        
@app.route('/quotes/<a>')
def id(a):
    manipulador = open('quotes.json','r')
    mp = json.load(manipulador)
    lista = [mp]
    for i in lista:
        return jsonify(i[int(a)])
     
                   
@app.route('/quotes/length')
def lenn():
    manipulador = open('quotes.json','r')
    mp = json.load(manipulador)
    for i, e in enumerate(mp):
        i+= 1
    return str(i)  

        
if __name__ == "__main__":
    app.run(debug=True)  