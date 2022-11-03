class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    def del_owner(self):
        del self._owner

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance > 0:
            self._balance = balance

    def del_balance(self):
        del self._balance

    def __str__(self):
        return f"{self._owner} has ${self._balance} on account."

    owner = property(get_owner, set_owner, del_owner, "owner property")
    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance, doc="balance")
