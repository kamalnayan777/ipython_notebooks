from flask import Flask

app = Flask(__name__)

@app.route("/Hello_flask")
def hello_flask234():
    return "<p>Hello Flask </p>"

@app.route("/")
def intro():
    return "<p>Hello WOrld</p>"






if __name__ =='__main__':
    app.run()