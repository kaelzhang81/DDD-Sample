# coding=utf-8

import value_object

class Delivery(object):
    def __init__(self, after_days):
        self._after_days = after_days

    @property
    def after_days(self):
        return self._after_days


ValueObject.register(Delivery)

if __name__ == '__main__':
    print 'Subclass:', issubclass(Delivery, ValueObject)
    print 'Instance:', isinstance(Delivery, ValueObject)
