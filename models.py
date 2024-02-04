"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

DEFAULT_IMAGE= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuyXLZ8jVosoKI3zWfW42v7xuk8uzwxhAvZA&usqp=CAU'

class Cupcake(db.Model):
    """create instances of cupcakes"""
    
    __tablename__ = 'cupcakes'
    
    id= db.Column(db.Integer,primary_key=True, autoincrement=True)
    flavor= db.Column(db.Text, nullable=False)
    size=db.Column(db.Text, nullable=False)
    rating= db.Column(db.Float, nullable=False)
    image= db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)
    
    def to_dict(self):
        """serialize cupcake to dictionary"""
        
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image,   
        }
def connect_db(app):
    """connect to database"""
    
    db.app= app
    db.init_app(app)