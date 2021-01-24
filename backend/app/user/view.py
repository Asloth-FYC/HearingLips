from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)


@user_bp.route('/',methods=['GET','POST'])
def index():
    return 'welcome! Vue+Flask!'
