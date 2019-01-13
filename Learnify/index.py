from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Learnify.auth import login_required
from Learnify.db import get_db

from scraper import return_link

bp = Blueprint('main', __name__)

def create():

    return redirect(url_for('index'))


@bp.route('/')
def index():

    links = ["hello.com", "bye.org"]

    return render_template('mainpage.html', links=links)


@bp.route('/', methods=('GET',))
@login_required
def search_sites():
    query = request.form.get('temp')
    error = None
    link = "if you see this, Link is none"

    if not query:
        error = "cannot read from form"

    if error is not None:
        flash(error)

    else:
        # db = get_db()
        link = return_link(query)

    return render_template('mainpage.html', link=link)
