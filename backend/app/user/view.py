from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)


@user_bp.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'hello! Vue&Flask!'
