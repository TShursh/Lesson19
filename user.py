class User:
    __number = 0
    __count = 0

    def __init__(self):
        User.__number += 1
        User.__count += 1
        self._id = User.__number

    def get_id(self):
        return self._id

    def __str__(self):
        return f"User with id = {self._id}"

    def __del__(self):
        User.__count -= 1

    def get_count():
        return User.__count

u1 = User()
u2 = User()
u3 = User()

print(u1)
print(u2)
print(u3)
print(f"Total user: {User.get_count()}")