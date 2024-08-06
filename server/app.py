from config import app, api
from flask import make_response, render_template
from flask_restful import Resource
from models import User


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        print(users)
        return users, 200
api.add_resource(Users, '/api/users')