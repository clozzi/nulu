from config import app, api, db
from flask import render_template, request, session
from flask_restful import Resource
from models import User, Media


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")

class Login(Resource):
    def post(self):
        name = request.get_json()['name']
        password = request.get_json()['password']
        user = User.query.filter_by(name=name).first()
        if user:
            if user.password == password:
                session['user_id'] = user.id
                return user.to_dict()
            else:
                return {'error': 'Incorrect password'}, 400
        else:
            return {'error': 'User not found'}, 400
api.add_resource(Login, '/api/login')

class Signup(Resource):
    def post(self):
        name = request.get_json()['name']
        password = request.get_json()['password']
        user = User.query.filter_by(name=name).first()
        if user:
            return {'error': 'Username taken.'}, 400
        else:
            try:
                new_user = User(
                    name=name,
                    password=password,
                )
                db.session.add(new_user)
                db.session.commit()
                session['user_id'] = new_user.id
                return new_user.to_dict(), 200
            except:
                return {'error': 'Could not create user'}, 400
api.add_resource(Signup, '/api/signup')

class CheckSession(Resource):
    def get(self):
        id = session.get('user_id')
        if id:
            user = User.query.filter_by(id=id).first()
            return user.to_dict()
        else:
            return {'error': 'Not Authorized'}, 401
api.add_resource(CheckSession, '/api/check_session')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {'message': 'Logged out'}, 204
api.add_resource(Logout, '/api/logout')


class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200
api.add_resource(Users, '/api/users')

class Medias(Resource):
    def get(self):
        medias = [media.to_dict() for media in Media.query.all()]
        return medias, 200
api.add_resource(Medias, '/api/medias')