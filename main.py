from flask import Flask
app = Flask(__name__)
@app.route('/')
with open("test.txt", 'w') as f:
    f.write("test")
def test():
    with open("test.txt", 'r') as f:
        c = f.readlines()
    return c
