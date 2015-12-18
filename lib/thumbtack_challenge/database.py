import os.path
from thumbtack_challenge.store import Store


class Database:

    def __init__(self):
        self.db = 'data/data.txt'
        self.auto_commit = True
        self.buffer = []
        data = '{}'
        if os.path.isfile(self.db):
            with open(self.db) as f:
                data = f.read()
        self.storage = Store(data)

    def begin(self, args):
        self.auto_commit = False
        self.buffer.append(Store('{}'))

    def rollback(self, args):
        if self.buffer:
            self.buffer[-1].reset()
            self.buffer.pop()
        else:
            print('NO TRANSACTION')

    def commit(self, args):
        if self.buffer:
            self.auto_commit = True
            for buffer in self.buffer:
                for name, value in buffer.items():
                    self.storage.set(name, value)
                buffer.reset()
            self.buffer = []
            with open(self.db, 'w+') as f:
                f.write(str(self.storage))
        else:
            print('NO TRANSACTION')

    def get(self, args):
        if self.storage.get(args[1]):
            return print(self.storage.get(args[1]))
        self.buffer.reverse()
        for buffer in self.buffer:
            if buffer.get(args[1]):
                self.buffer.reverse()
                return print(buffer.get(args[1]))
        self.buffer.reverse()

    def unset(self, args):
        if self.auto_commit:
            self.storage.unset(args[1])
        else:
            if self.buffer:
                self.buffer[-q].unset(args[1])

    def numequalto(self, args):
        value = args[1]
        result = 0
        checklist = {}
        for buffer in self.buffer:
            for name, stored_value in buffer.items():
                if stored_value == value and name not in checklist:
                    checklist[name] = 1
                    result += 1
        for name, stored_value in self.storage.items():
            if stored_value == value and name not in checklist:
                checklist[name] = 1
                result += 1
        print(result)

    def set(self, args):
        if self.auto_commit:
            self.storage.set(args[1], args[2])
        else:
            if not self.buffer:
                self.buffer = [Store('{}')]
            self.buffer[-1].set(args[1], args[2])
