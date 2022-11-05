from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "ola mundo"

@app.route("/health")
def health():
        return "OK"
count=0

@app.route("/counter")
def counter():
    global count
    count+=1
    return str(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=(os.environ.get("APP_PORT")), debug=True)
