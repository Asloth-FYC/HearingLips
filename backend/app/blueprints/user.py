from flask import Blueprint, request, jsonify, json
from app.extensions import db
from app.models import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/regi', methods=['POST', 'GET'])
def register():
    post_data = json.loads(request.get_data(as_text=True))
    name = post_data['name']
    email = post_data['email']
    psw = post_data['psw']
    user = User.query.filter(User.email == email).all()
    if user:
        return jsonify(code=400, msg='该邮箱已被注册！')
    else:
        user = User()
        user.email = email
        user.username = name
        user.password = psw
        db.session.add(user)
        db.session.commit()
        return jsonify(code=200, msg='注册成功！')


@user_bp.route('/login', methods=['POST'])
def login():
    post_data = json.loads(request.get_data(as_text=True))
    email = post_data['email']
    psw = post_data['psw']
    user = User.query.filter(User.email == email).first()
    if user:
        if user.password == psw:
            return jsonify(code=200, name=user.username, msg='登录成功！')

    return jsonify(code=400, msg='用户名或密码错误！')