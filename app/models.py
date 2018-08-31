from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_login import current_user
import sqlalchemy_utils
from app import db, blueprint
from datetime import datetime


class Instances(db.Model):
    """ This Class Store Detail of the Server"""
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ip = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    dbUser = db.Column(db.String(100), nullable=False)
    dbName = db.Column(db.String(100), nullable=False)
    dbPass = db.Column(db.String(100), nullable=False)
    sshUser = db.Column(db.String(100), nullable=False)
    sshPass = db.Column(db.String(100), nullable=False)


class User(db.Model):
    """ This Class Store the Detail of the User"""
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    tokens = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())


class OAuth(db.Model,OAuthConsumerMixin):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


class Roles(db.Model):
    """ This Class Store the Role of the User"""
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role = db.Column(db.String(100), nullable=True)
    capabilities = db.Column(db.String(200), nullable=True)


# storage = SQLAlchemyBackend(OAuth, db.session, user=current_user)
# blueprint.backend = storage
