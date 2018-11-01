from flask import Flask, request, flash, render_template, url_for
import os

app = Flask(__name__)
app.config.from_object(__name__)
env = os.environ.copy()

if 'SECRET_KEY' in env:
    SECRET_KEY = env['SECRET_KEY']
    app.secret_key = SECRET_KEY


@app.route("/", methods=['GET', 'POST'])
def home():
    url_for('static', filename='style.css')

    return render_template(
        'index.html',
    )
