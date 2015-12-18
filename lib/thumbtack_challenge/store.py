import json


class Store:

    def __init__(self, data):
        self._store = json.loads(data)

    def get(self, name):
        return self._store.get(name, None)

    def items(self):
        return self._store.items()

    def reset(self):
        self._store = {}

    def set(self, name, value):
        self._store[name] = value

    def unset(self, name):
        if name in self._store:
            self._store.pop(name)

    def __str__(self):
        return json.dumps(self._store)
