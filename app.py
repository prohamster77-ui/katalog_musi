from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_data():
    # Mengambil data dari products.json
    with open('products.json', 'r') as f:
        return json.load(f)

@app.route('/')
def katalog():
    items = load_data()
    return render_template('index.html', products=items)

if __name__ == '__main__':
    app.run(debug=True)