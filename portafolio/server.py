from flask import Flask
from flask import request 
from flask import render_template
from flask import redirect



app = Flask(__name__)



@app.get('/')
def paola():
    return render_template('index.html')


    
if __name__ == '__main__':
    app.run('0.0.0.0', 7676, debug=True)
