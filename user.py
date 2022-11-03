class User:
    number = 0
    count = 0

    def __init__(self):
        User.number += 1
        User.count += 1
        self._id = User.number

    def get_id(self):
        return self._id

    def __str__(self):
        return f"User with id = {self._id}"

    def __del__(self):
        User.count -= 1


u1 = User()
u2 = User()
u3 = User()

print(u1)
print(u2)
print(u3)
