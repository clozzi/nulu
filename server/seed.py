from app import app
from models import db, User

with app.app_context():
    print('Deleting users...')
    User.query.delete()

    print('Creating users...')
    One = User(name='One', password='123')
    Two = User(name='Two', password='123')
    Three = User(name='Three', password='123')
    Four = User(name='Four', password='123')
    Five = User(name='Five', password='123')

    print('Adding users...')
    db.session.add_all([One, Two, Three, Four, Five])

    print('Committing...')
    db.session.commit()

    print('Seed Successful!')