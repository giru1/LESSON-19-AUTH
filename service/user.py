from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register(self, data: dict) -> dict:
       return self.dao.create(data)














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
