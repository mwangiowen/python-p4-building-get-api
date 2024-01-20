# app/app.py

#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  # Create the db instance

migrate = Migrate(app, db)

# Import your models
from models import User, Review, Game


@app.route("/")
def index():
    return "Index for Game/Review/User API"


@app.route("/games")
def games():
    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)

    response = make_response(jsonify(games), 200)
    response.headers["Content-Type"] = "application/json"

    return response


@app.route("/games/<int:id>")
def game_by_id(id):
    game = Game.query.get(id)

    if game:
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        response = make_response(jsonify(game_dict), 200)
    else:
        response = make_response(jsonify({"error": "Game not found"}), 404)

    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == "__main__":
    app.run(port=5555)
