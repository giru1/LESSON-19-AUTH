import base64
import hashlib
from datetime import timedelta, datetime
from typing import Dict

import jwt

import constants


def get_hashed_pass(password: str) -> str:
    return base64.b64encode(hashlib.pbkdf2_hmac(
        hash_name=constants.HASH_NAME,
        salt=constants.HASH_SALT.encode('utf-8'),
        iterations=constants.HASH_GEN_ITERATIONS,
        password=password.encode('utf-8')
    )).decode('utf-8', "ignore")


def genereta_tokens(data: dict) -> Dict[str, str]:
    data['exp'] = datetime.utcnow() + timedelta(minutes=30)
    data['refresh_token'] = False

    access_token: str = jwt.encode(
        payload=data,
        key=constants.SECRET_HERE,
        algorithm=constants.JWT_ALGORITHM,
    )

    data['exp'] = datetime.utcnow() + timedelta(days=30)
    data['refresh_token'] = True

    refresh_token: str = jwt.encode(
        payload=data,
        key=constants.SECRET_HERE,
        algorithm=constants.JWT_ALGORITHM,
    )

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
