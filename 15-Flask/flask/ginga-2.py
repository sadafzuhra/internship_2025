
## variable rule 
## ginja 2 template
from flask import Flask, render_template, request


# WSGI

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Microinformatics, it's the home page. Haseeb Raza is a DS." 

@app.route('/about')
def about():
    return "<html><h1>Biotech and Data Science Education Start-Up</h1><html>"

@
### HTTP verbs, ## GET, POST


@app.route('/submit/<score>')
def submit():
    if score>=40:
        return 'you are passed the exam "+" congratulation'
        



if __name__=="__main__":
    app.run(debug=True)