import uuid
from app.extensions import mail
from flask import Blueprint, json, request, session, jsonify
from flask_mail import Message

email_bp = Blueprint('email', __name__)


@email_bp.route('/captcha', methods=['POST', 'GET'])
def captcha():
    post_data = json.loads(request.get_data(as_text=True))
    email = post_data['email']
    type = post_data['type']
    email_captcha = str(uuid.uuid1())[:6]
    if type == 1:
        message = Message('欢迎注册HearingLips!', recipients=[email],
                          body='【HearingLips】 欢迎您注册HearingLips，您的验证码是：%s' % email_captcha + '。验证码有效时间5分钟，请勿将验证码泄漏于他人。若非本人操作，请忽略此信息。')
    elif type == 2:
        message = Message('找回密码', recipients=[email],
                          body='【HearingLips】 您正在使用邮箱找回密码，您的验证码是：%s' % email_captcha + '。验证码有效时间5分钟，请勿将验证码泄漏于他人。若非本人操作，请忽略此信息。')
    try:
        mail.send(message)  # 发送
    except:
        return jsonify(code=400, msg='服务器出错了')
    session['captcha'] = email_captcha
    return jsonify(code=200, msg='验证码已发送，请尽快填写！')
