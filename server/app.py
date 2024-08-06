from config import app, api
from flask import render_template
from flask_restful import Resource
from models import User, Media


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        print(users)
        return users, 200
api.add_resource(Users, '/api/users')

class Medias(Resource):
    def get(self):
        medias = [media.to_dict() for media in Media.query.all()]
        print(medias)
        return medias, 200
api.add_resource(Medias, '/api/medias')