from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index() :
    return ("<h1>Hello World</h1>")

@app.route('/networks/<lab>') 
def lab(lab) :
    return render_template(lab + ".html")


if __name__ == "__main__" :
    app.run(port = 5001)