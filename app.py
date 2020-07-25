from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////testing.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(140))
    price=db.Column(db.Numeric())
    description=db.Column(db.Text)

@app.cli.command()
def createdb():
    db.create_all()

@app.route('/')
def inicio():
    return "Olá visitante"

@app.route('/products')
def index():
    products=Products.query.all()
    return render_template("index.html", products=products)

@app.route('/products/<product_id>')
def product(product_id):
    product=Products.query.filter_by(id=product_id).first() or abort(404, 'Produto não encontrado')
    return render_template("product.html", product=product)