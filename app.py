from flask import Flask 
App= Flask(__name__)
@app.route('/')

def home():
    return 'Hello,web!'


app.run(debug=True)