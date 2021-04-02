"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


# Functions start here!

def create_user(e, passcode):
    """Create and return a new user."""

    new_user = User(email=e, password=passcode)

    db.session.add(new_user)
    db.session.commit()

    return new_user
    

def create_movie(name, summary, date, poster):
    """Create and return a new movie."""

    new_movie = Movie(title=name, overview=summary, release_date=date, poster_path=poster)
    
    db.session.add(new_movie)
    db.session.commit()

    return new_movie


def create_rating(user_edit, current_movie, new_score):
    """Create and return a new rating."""

    new_rating = Rating(user=user_edit, movie=current_movie, score=new_score)

    db.session.add(new_rating)
    db.session.commit()

    return new_rating




if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)
