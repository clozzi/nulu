from sqlalchemy_serializer import SerializerMixin
from config import db


user_medias = db.Table(
    "users_medias",
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True),
    db.Column("media_id", db.ForeignKey("medias.id"), primary_key=True),
)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    medias = db.relationship('Media', secondary=user_medias, back_populates="users")

    def __repr__(self):
        return f'User {self.name}'
    

class Media(db.Model, SerializerMixin):
    __tablename__ = 'medias'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    media_type = db.Column(db.String)
    genre = db.Column(db.String)
    img = db.Column(db.String)
    users = db.relationship('User', secondary=user_medias, back_populates="medias")

    def __repr__(self):
        return f'Media {self.title} | {self.description} | {self.img}'