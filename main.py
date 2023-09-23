from flask import Flask
app = Flask(__name__)
@app.route('/')
def test():
    with open("test.txt", 'r') as f:
        c = f.readlines()
    return c
