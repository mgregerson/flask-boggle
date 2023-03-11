from flask import Flask, request, render_template, jsonify
from uuid import uuid4
import json

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""
    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    # game_id = str(uuid4())
    # game = BoggleGame()
    # games[game_id] = game

    game_id = str(uuid4())
    game = BoggleGame()
    game_board = []
    games[game_id] = game

    for line in game.board:
        game_board.append(tuple(line))

    response = {
        "game_id": game_id,
        "board": game_board
    }

    games[f"{game_id}"] = response
    print(games)
    return jsonify(response)
