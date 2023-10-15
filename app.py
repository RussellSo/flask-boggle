from boggle import Boggle
from flask import Flask, session, render_template, redirect, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretdog"

boggle_game = Boggle()


@app.route("/")
def home():
    board = boggle_game.make_board()
    session["board"] = board

    return render_template("home.html", board=board)

# huge discovery - steps 1. js get method needs , {params : {}} - that param key becomes the arg
@app.route("/guesses")
def guesses():
    guess = request.args['guess']
    board = session['board']
    check_word = boggle_game.check_valid_word(board, guess)
    return jsonify(
        {"res": check_word} ## either 'ok' 'not-word' 'not-on-board'
    )


## check how many times user has played - something about request.json - 10 mins
## how to handle duplicate words? - maybe set - 10 mins
## tests - 30 mins
## 1hour total