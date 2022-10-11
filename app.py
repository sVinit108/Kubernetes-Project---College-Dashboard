
from flask import Flask, request,render_template


app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def permission():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")