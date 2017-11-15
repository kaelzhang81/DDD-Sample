# coding=utf-8

import abc

class Factory(object):
    metaclass=abc.ABCMeta

    @abstractmethod
    def create(self):
        raise NotImplementedError
