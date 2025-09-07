#blue.py
from flask import Blueprint, url_for 
from flask import redirect
bp = Blueprint('blue', __name__, url_prefix='/')

@bp.route("/hello")
def print_blue():
	return "hello Pybo!"

@bp.route("/")
def index():
    return redirect(url_for('question._list'))

