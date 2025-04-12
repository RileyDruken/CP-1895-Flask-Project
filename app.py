from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/removal')
def removal():
    return render_template('removal.html')


if __name__ == '__main__':
    app.run()
