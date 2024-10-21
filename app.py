from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index() :
    return redirect("/networks/lab_1")

@app.route('/networks/<lab>') 
def lab(lab) :
    return render_template(lab + ".html")

app.run(port = 5001, debug=True)