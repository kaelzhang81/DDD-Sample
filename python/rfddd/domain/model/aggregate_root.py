# coding=utf-8

from .entity import Entity


class AggregateRoot(Entity):
    def __init__(self, id):
        self._id = id

    def get_id(self):
        return self._id
