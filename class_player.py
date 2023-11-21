import sys


class Player:
    def __init__(self, name='Jeff', balance=1000):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @name.setter
    def name(self, value):
        self._name = value

    @balance.setter
    def balance(self, value):
        self._balance = value

    def change_balance(self, amount):
        self._balance += amount

    def bet(self, amount):
        self._balance -= amount

    def check_balance(self):
        if self._balance == 0:
            print(f'You are out of chips')
            sys.exit()

    def print(self):
        print(f'Name: {self._name}\nKontostand: {self._balance}')


if __name__ == '__main__':
    test = Player('Ich bin eine Test', 1000)
    test.print()
    print('----------------')
    test.change_balance(1000)
    test.print()
    print('----------------')
    test.bet(500)
    test.print()
