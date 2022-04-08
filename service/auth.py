from flask import request

from dao.auth import AuthDAO
from flask_restx import abort
from utils import get_hashed_pass, genereta_tokens, decode_token


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    def login(self, data: dict):
        user_data = self.dao.get_by_username(data['username'])
        print(data)
        if user_data is None:
            abort(401, message='user not found')

        hashed_pass = get_hashed_pass(data['password'])
        if user_data['password'] != hashed_pass:
            abort(401, message='No correct data')

        tokens: dict = genereta_tokens(
            {
                'username': data['username'],
                'role': user_data['role']
            }
        )
        return tokens


    def get_new_token(self, refresh_token: str):
        decoded_token = decode_token(refresh_token, refresh_token=True)

        token = genereta_tokens(
            data={
                'username': decoded_token['username'],
                'role': decoded_token['role']
            }
        )
        return token

