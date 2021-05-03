import os
import _thread

import cv2

from app.extensions import db
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.models import Project
from app.settings import basedir
from app.utils import verify_auth_token

project_bp = Blueprint('project', __name__)


@project_bp.route('/api/upload', methods=['POST', 'GET'])
def upload():
    formData = request.form.to_dict()
    token = formData.get('token')
    data = verify_auth_token(token)
    if data:
        file = request.files.get('file')
        filename = secure_filename(file.filename)
        project = Project()
        project.type = formData.get('type')
        project.name = formData.get('name')
        project.url = os.path.join(os.getenv('FILE_URL_PREFIX'), filename)
        project.user_id = data['user_code']

        file_path = os.path.join(basedir, 'static/', filename)
        file.save(file_path)
        # 制作封面
        vidcap = cv2.VideoCapture(file_path)
        success, image = vidcap.read()
        cv2.imencode('.jpg', image)[1].tofile(os.path.join(basedir, 'static/') + "/%s.jpg" % filename)

        # os.system("start python E:\HearingLips\\backend\\app\dl\ops\\utils.py %s" %(filename))
        os.system("python /www/backend/app/dl/ops/utils.py %s &" %(filename))
        # 在Linux平台上 只需要在命令末尾加上shell后台运算符&  windows : start

        db.session.add(project)
        db.session.commit()
        return jsonify(code=200, msg='上传成功')
    else:
        return jsonify(code=400, msg='上传失败')
