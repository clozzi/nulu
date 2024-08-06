from app import app
from models import db, User, Media

with app.app_context():
    print('Deleting users...')
    User.query.delete()
    print('Deleting medias...')
    Media.query.delete()

    print('Creating users...')
    One = User(name='One', password='123')
    Two = User(name='Two', password='123')
    Three = User(name='Three', password='123')
    Four = User(name='Four', password='123')
    Five = User(name='Five', password='123')

    print('Creating movies...')
    MovieOne = Media(title="MovieOne", description="Dope.", img="https://cdn.pixabay.com/photo/2019/04/24/21/55/cinema-4153289_1280.jpg")
    MovieTwo = Media(title="MovieTwo", description="Dope.", img="https://cdn.pixabay.com/photo/2019/04/24/21/55/cinema-4153289_1280.jpg")
    MovieThree = Media(title="MovieThree", description="Dope.", img="https://cdn.pixabay.com/photo/2019/04/24/21/55/cinema-4153289_1280.jpg")
    MovieFour = Media(title="MovieFour", description="Dope.", img="https://cdn.pixabay.com/photo/2019/04/24/21/55/cinema-4153289_1280.jpg")
    MovieFive = Media(title="MovieFive", description="Dope.", img="https://cdn.pixabay.com/photo/2019/04/24/21/55/cinema-4153289_1280.jpg")

    print('Creating tv...')
    TVOne = Media(title="TVOne", description="Dope.", img="https://cdn.pixabay.com/photo/2024/01/21/20/09/ai-generated-8523907_1280.png")
    TVTwo = Media(title="TVTwo", description="Dope.", img="https://cdn.pixabay.com/photo/2024/01/21/20/09/ai-generated-8523907_1280.png")
    TVThree = Media(title="TVThree", description="Dope.", img="https://cdn.pixabay.com/photo/2024/01/21/20/09/ai-generated-8523907_1280.png")
    TVFour = Media(title="TVFour", description="Dope.", img="https://cdn.pixabay.com/photo/2024/01/21/20/09/ai-generated-8523907_1280.png")
    TVFive = Media(title="TVFive", description="Dope.", img="https://cdn.pixabay.com/photo/2024/01/21/20/09/ai-generated-8523907_1280.png")

    print('Adding users...')
    db.session.add_all([One, Two, Three, Four, Five])

    print('Adding media...')
    db.session.add_all([MovieOne, MovieTwo, MovieThree, MovieFour, MovieFive, TVOne, TVTwo, TVThree, TVFour, TVFive])

    print('Committing...')
    db.session.commit()

    print('Seed Successful!')