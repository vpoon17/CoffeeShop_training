# project/server/models.py
from datetime import datetime

from sqlalchemy_utils import URLType

from coffeeshop.server import db
from ..models import User


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    address = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    url = db.Column(URLType)
    photo = db.Column(db.String)  # store the URL location of uploaded photos, or perhaps just the filename.
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User, backref=db.backref('shops'))

    def __repr__(self):
        return f'<Shop name={self.name} address={self.address} location=POINT ({self.longitude} {self.latitude}) url={self.url} photo={self.photo} user={self.user_id}>'


class Review(db.Model):
    __tablename__ = 'review'

    SCORES = [
        (0, 'Bad'),
        (1, 'Good')
    ]

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    shop = db.relationship(Shop, backref=db.backref('reviews', lazy='joined'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User, backref=db.backref('reviews'), lazy='joined')

    def __repr__(self):
        return f'<Review rating={self.rating} shop={self.shop_id} user={self.user_id}>'
