from flask import Flask

app = Flask(__name__)

@app.route("/") ##path after the domain name
def hello_world():
    return "Hello World!" ##when this url is access show Hello World

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)