from flask import Flask
app = Flask(__name__)
with open("test.txt", 'w') as f:
    f.write("test")
@app.route('/')
def test():
    with open("test.txt", 'r') as f:
        c = f.readlines()
    return c
