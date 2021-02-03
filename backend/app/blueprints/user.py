from flask import Blueprint, request, jsonify, json
from app.extensions import db
from app.models import User
from app.utils.token import generate_auth_token, verify_auth_token

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
        return jsonify(code=200, msg='欢迎加入HearingLips！')


@user_bp.route('/login', methods=['POST'])
def login():
    post_data = json.loads(request.get_data(as_text=True))
    email = post_data['email']
    psw = post_data['psw']
    user = User.query.filter(User.email == email).first()

    if user:
        if user.password == psw:
            return jsonify(code=200, name=user.username, id=user.id, token=generate_auth_token(user.id), msg='登录成功！')

    return jsonify(code=400, msg='用户名或密码错误！')


@user_bp.route('/get', methods=['POST'])
def get():
    token = request.headers.get('token')
    data = verify_auth_token(token)
    if data is None:
        return jsonify(code=401, msg='登录过期，请重新登录！')
    user_id = data['user_code']
    user = User.query.get(user_id)

    return jsonify(code=200, data={'username':user.username}, msg='验证通过')
