from flask import Flask, render_template, request


solar = Flask(__name__) # initializng the flask app


@solar.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    solar .run(debug = False, port = 8000)