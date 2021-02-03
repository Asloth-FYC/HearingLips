import os
from app.extensions import db
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.models import Project
from app.settings import basedir
from app.utils import verify_auth_token

project_bp = Blueprint('project', __name__)


@project_bp.route('/upload', methods=['POST', 'GET'])
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
        file.save(os.path.join(basedir, 'static/', filename))
        db.session.add(project)
        db.session.commit()
        return jsonify(code=200, msg='上传成功')
    else:
        return jsonify(code=400, msg='上传失败')
