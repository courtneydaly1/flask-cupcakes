"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import Cupcake, db, connect_db
from flask_cors import CORS, cross_origin

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY']= 'shhSecret!'

connect_db(app)
app.app_context().push()

@app.route('/')
def homepage():
    """render homepage"""
    
    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """return ALL cupcakes available from api in JSON"""

    cupcakes= [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """returns info about 1 cupcake in JSON"""
    
    cupcake= Cupcake.query.get_or_404(cupcake_id) 
    
    return jsonify(cupcake=cupcake.to_dict())


@app.route('/api/cupcakes', methods=['POST'])
@cross_origin(origin='*')
def create_cupcake():
    """adds a new cupcake to returns data about it"""
    
    data= request.json
    
    cupcake= Cupcake(
        flavor=data['flavor'],
        rating= data['rating'],
        size= data['size'],
        image= data['image'] or None
    )   
    
    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.to_dict()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods= ['PATCH'])
def update_cupcake(cupcake_id):
    """update cupcake using data in request, then show update"""
    
    data= request.json
    
    cupcake= Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor= data['flavor']
    cupcake.rating= data['rating']
    cupcake.size= data['size']
    cupcake.image=data['image']
    
    db.session.add(cupcake)
    db.session.commit()
    
    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def remove_cupcake(cupcake_id):
    """delete a specific cupcake, return confirm message""" 
    
    cupcake= Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message='Cupcake has been deleted.')      