# coding=utf-8


class Repository:
    def __init__(self):
        self._repo = {}

    def store(self, id, obj):
        if self._has_key(id):
            return False
        self._repo[id] = obj
        return True

    def delete(self, id):
        if self._has_key(self, id):
            del self._repo[id]

    def find(self, id):
        return self._repo.get(id)

    def _has_key(self, id):
        return self._repo.has_key(id)
