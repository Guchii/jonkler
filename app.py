from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import database.models
from socket_manager import SocketManager
from database.db import engine, get_db
from database.models import Base, User
from time import sleep
from sqlalchemy.orm import Session
from users import get_current_user, user_current_game_status, add_user_to_game
from game import create_game, Game, get_current_game

while True:
    try:
        Base.metadata.create_all(bind=engine)
        break
    except Exception as error:
        print("Connection failed: ", error)
        sleep(3)




game_flag = False
while True:
    if game_flag == False:
        uid = input("Enter user id to login: ")

        # Get current User
        user = get_current_user(int(uid))
        if not user:
            continue

        # Check if user is in a game
        existing_game = user_current_game_status(user.uid)
        if existing_game:
            game_flag = True
            game = Game(existing_game.game_id)
            game.users.append(user.uid)
    
    if not game_flag:
        print("Debug: I am here")
        user_action = int(input("1. Join Game\n2. Create Game "))
    
        if user_action == 1:
            join_game_id = int(input("Enter the game id you want to join: "))
            

        if user_action == 2:
            print("Debug: Creating Game")
            game = create_game()
            game.users.append(int(user.uid))
            add_user_to_game(int(user.uid), int(game.game_id))
            game_flag = True
            
    
    if game_flag:
        game.all_users()



# app = FastAPI()
# socket = SocketManager() 


# @app.websocket("/ws/{room}")
# async def websocket_endpoint(websocket: WebSocket, room: str):
#     await socket.connect(websocket, room)
#     try:
#         while True:
#             message =  await websocket.receive_text()
#             await socket.game_actions(room, message)

#     except WebSocketDisconnect:
#         socket.connections[room]['connections'].remove(websocket)
#         del websocket

# @app.get("/")
# async def get():
#     return "Hello World"