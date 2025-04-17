from flask import Flask, render_template, request, session, redirect
from werkzeug.utils import secure_filename
import os, datetime

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static/uploads")
app.config['MAX_CONTENT_LENGTH'] = 15 * 1024 * 1024
app.secret_key = os.getenv("SECRET_KEY")


@app.route('/')
def index():
    if session.get('games') == None:
        session['games'] = []

    found_fav = 0
    for game in session['games']:
        if game[4] == 1:
            found_fav = 1

    if found_fav:
        return render_template('index.html', games=session['games'])
    return render_template('index.html', games=session['games'], message="Favourites will appear here")


@app.route('/games')
def games():
    if "games" in session:
        print(session["games"])
        return render_template('games.html', games=session["games"])
    return render_template('games.html')


@app.route('/favourite', methods=["POST"])
def favourite():
    if session.get('games') == None:
        session['games'] = []

    gamesList = session['games']
    for game in gamesList:
        if game[3] == request.form.get("favouriteButton"):
            if game[4] == 1:
                game[4] = 0
            elif game[4] == 0:
                game[4] = 1

    session['games'] = gamesList

    return render_template('games.html', games=session["games"])


@app.route('/removal', methods=['GET', 'POST'])
def removal():
    if request.method == "POST":
        if session.get('games') != None:
            for i in session["games"]:
                if request.form["button"] in i:
                    session["games"].remove(i)
        gamesList = session['games']
        session['games'] = gamesList
    if "games" in session:
        return render_template('removal.html', games=session["games"])
    return render_template('removal.html')


@app.route('/add', methods=["GET", "POST"])
def add():
    game = []
    if request.method == "POST":
        name = request.form["name"]
        genre = request.form["genre"]
        platform = request.form["platform"]
        picture = request.files.get("picture")

        if name == "" or genre == "" or platform == "":
            return render_template('add.html', error="Please fill all fields")

        if picture.content_type == "image/jpeg" or picture.content_type == "image/jpg" or picture.content_type == "image/png":

            filename = secure_filename(picture.filename)
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            uniquename = timestamp + filename

            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], uniquename))

            game.append(name)
            game.append(genre)
            game.append(platform)
            game.append(uniquename)
            game.append(0)

        else:
            return render_template('add.html', error="Image File type not supported or is empty")
        if session.get("games") == None:
            gamesList = []
        else:
            gamesList = session['games']
        gamesList.append(game)
        session['games'] = gamesList
        return render_template('games.html', games=session["games"])
    return render_template('add.html')


@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template('add.html', error="File too large")


if __name__ == '__main__':
    app.run()
