from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Learnify.auth import login_required
from Learnify.db import get_db

from scraper import return_link

bp = Blueprint('index', __name__)

def create():

    return redirect(url_for('index'))


@bp.route('/')
def index():

    links = ["hello.com", "bye.org"]

    return render_template('index.html', links=links)


@bp.route('/', methods=['POST'])
@login_required
def search_sites():
    query = request.form['text']
    error = None
    link = None

    if not query:
        error = "enter something"

    if error is not None:
        flash(error)

    else:
        # db = get_db()
        link = return_link(query)

    return render_template('index.html', link=link)
