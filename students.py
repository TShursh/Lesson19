class Student:
    """class description of student"""

    def __init__(self, name, age, mark=4, alive=True):
        self._name = name
        self._age = age
        self._mark = mark
        self._alive = alive

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 16:
            self._age = age

    def del_age(self):
        del self._age

    def get_mark(self):
        return self._mark

    def set_mark(self, mark):
        self._mark = mark

    def del_mark(self):
        del self._mark

    def get_alive(self):
        return self._alive

    def set_alive(self, alive):
        self._alive = alive

    def del_alive(self):
        del self._alive

    def __str__(self):
        msg = self._name
        msg += (" is still alive "
                if self._alive else " is dead ")
        msg += "(mark: " + str(self._mark) + ")"

        return msg

    name = property(get_name, set_name, del_name)
    age = property(get_age, set_age, del_age)
    mark = property(get_mark, set_mark, del_mark)
    alive = property(get_alive, set_alive, del_alive)