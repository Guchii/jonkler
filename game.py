from icecream import ic
from database.db import get_db
import database.models as model
from sqlalchemy.orm import Session


class Game:

    users = []

    def __init__(self, game_id = None):
        self.game_id = game_id


    def all_users(self):
        print(self.users)

    


def create_game() -> Game:
    db: Session = next(get_db())

    try:
        game = model.Game()
        db.add(game)
        db.commit()
        db.refresh(game)
    finally:
        db.close()

    return Game(game.game_id)

def get_current_game(game_id: int) -> Game | bool:
    db: Session = next(get_db())
    try:
        game_q = db.query(model.Game).filter(
            model.Game.game_id == game_id
        )
        game = game_q.first()
    finally:
        db.close()
    
    if not game:
        return False
    
    # Users in game

    db: Session = next(get_db())
    try:
        game_q = db.query(model.ActiveGames).filter(
            model.ActiveGames.game_id == game_id
        )
        game_user_data = game_q.all()
    finally:
        db.close()
        
    existing_game = Game(game.game_id)

    if game_user_data:
        for record in game_user_data:
            existing_game.users.append(record.uid)
    else:
        print("This game does not have any user")
    
    return existing_game
