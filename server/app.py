from flask import make_response, jsonify
from config import app, api
from flask_restful import Resource
from models import User
from sqlalchemy_serializer import SerializerMixin


class Users(Resource, SerializerMixin):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        print(users)
        return users, 200
api.add_resource(Users, '/api/users')