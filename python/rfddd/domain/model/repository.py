# coding=utf-8
import abc

class Repository(object):
    metaclass=abc.ABCMeta

    @abstractmethod
    def add(self, , id, obj):
        raise NotImplementedError

    @abstractmethod
    def save(self, id, obj):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id):
        raise NotImplementedError
