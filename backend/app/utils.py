import os
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired


# 生成token, 有效时间为1d
def generate_auth_token(user_id, expiration=86400):
    # 第一个参数是内部私钥
    # 第二个参数是有效期（秒）
    s = Serializer(os.getenv('SECRET_KEY'), expires_in=expiration)
    token = s.dumps({'user_code': user_id}).decode("ascii")
    return token


def verify_auth_token(token):
    s = Serializer(os.getenv('SECRET_KEY'))
    # token正确
    try:
        data = s.loads(token)
        return data
    # token过期
    except SignatureExpired:
        return None
    # token错误
    except BadSignature:
        return None


# 对象转json
def class_to_dict(obj):
    obj_arr = []
    for o in obj:
        dict = {}
        a = o.__dict__
        if "_sa_instance_state" in a:
            del a['_sa_instance_state']
        dict.update(a)
        obj_arr.append(dict)
    return obj_arr

