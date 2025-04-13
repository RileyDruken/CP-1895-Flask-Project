from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os,datetime

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static/uploads")
app.config['MAX_CONTENT_LENGTH'] = 50000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/removal')
def removal():
    return render_template('removal.html')

@app.route('/add',  methods=["GET","POST"])
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
            print(game)
        else:
            return render_template('add.html', error="Image File type not supported or is empty")

    return render_template('add.html')

@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template('add.html' ,error="File too large")


if __name__ == '__main__':
    app.run()
