from src import UserRepo
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "Tá rodando fii"


@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepo()
    body = request.json

    userRepo.insert_user(body["name"])

    return f"Inseriu {body["name"]}"

