from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Домашняя страница',
                           username='Чел')


if __name__ == '__main__':
    app.run(port=5050, host='127.0.0.1')
