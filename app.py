from flask import Flask
import os
import random 

node_id=random.randint(1,1000)

app = Flask(__name__)

@app.route("/")
def hello_world():
    global node_id
    return "node:{}".format

@app.route("/health")
def health():
        return "OK"
count=0

@app.route("/counter")
def counter():
    global count
    count+=1
    return str(count) + "\n"

#app-flask:1.0.0
#docker build . -t app-flask:2.0.0
@app.route("/version")
def counter_route():
    return "2.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=(os.environ.get("APP_PORT")), debug=True)
