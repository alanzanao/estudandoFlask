from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
    return "Olá visitante"

@app.route('/product')
def index():
    products = {'name':'pão de sal', 'price':'0.5', 'description':'Very good'}
    return render_template("index.html", products=products)

@app.route("/product/<product_id>")
def product(product_id):
    products = {'name':'pão de sal', 'price':'0.5', 'description':'Very good'}
    return render_template("product.html", products=products)
     