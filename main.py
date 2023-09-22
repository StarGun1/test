from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open("test.txt", 'w') as f:
        f.write("test")
    with open("test.txt", 'r') as f:
        c = f.readlines()
    return c
  
