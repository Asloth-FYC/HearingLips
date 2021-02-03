import os

from flask import Blueprint, json, request
from werkzeug.utils import secure_filename

from app.settings import basedir

project_bp = Blueprint('project', __name__)


@project_bp.route('/upload', methods=['POST', 'GET'])
def upload():
    file = request.files.get('file')
    filename = secure_filename(file.filename)
    data = request.form
    print(data)
    print(file)
    file.save(os.path.join(basedir, 'static/', filename))
    return '收到'
