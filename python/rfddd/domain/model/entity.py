# coding=utf-8

import abc

class Entity(object):
    metaclass=abc.ABCMeta

    _instance_id_generator = count()

    def __init__(self, id):
        self._id = id
        self._instance_id = next(Entity._instance_id_generator)

    @property
    def instance_id(self):
        return self._instance_id

    @property
    def id(self):
        return self._id
