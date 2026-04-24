from user import User
from exceptions import UserNotFoundException


class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, name, age):
        user = User(name, age)
        self.users[name] = user
        return user

    def get_user(self, name):
        if name not in self.users:
            raise UserNotFoundException("User not found")
        return self.users[name]