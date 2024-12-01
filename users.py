from database.db import get_db
import database.models as model
from schema.users_schema import User
from sqlalchemy.orm import Session


def get_current_user(uid: int) -> User:

    db: Session = next(get_db())
    curr_user = db.query(model.User).filter(
        model.User.uid == uid
    )

    if not curr_user.first():
        print("No user found with ID:", uid)
        return False
    
    return curr_user.first()


def user_current_game_status(uid: int) -> model.ActiveGames:
    db: Session = next(get_db())
    
    curr_user_game = db.query(model.ActiveGames).filter(
        model.ActiveGames.uid == uid
    )

    curr_game = curr_user_game.first()

    if not curr_game:
        return False
    
    return curr_game

def add_user_to_game(uid, game_id):
    db: Session = next(get_db())

    active_game = model.ActiveGames(uid=uid, game_id=game_id)
    db.add(active_game)
    db.commit()
    db.refresh(active_game)
