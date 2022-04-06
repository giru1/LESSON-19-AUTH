from dao.user import UserDAO
from utils import get_hashed_pass


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register(self, data: dict) -> dict:
        data['password'] = get_hashed_pass(data['password'])
        self.dao.create(data)
        return data

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
