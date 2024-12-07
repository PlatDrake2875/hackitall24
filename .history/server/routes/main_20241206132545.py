from flask import Blueprint, render_template
from datetime import datetime
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', title="Home Page", current_year=current_year)

