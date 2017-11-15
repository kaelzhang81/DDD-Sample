# coding=utf-8

import entity

class Cargo(object):
    def __init__(self, id, delivery):
        self._id = id
        self._instance_id = next(Entity._instance_id_generator)
        slef._delivery = delivery

    def delay(days):
        after = self._delivery.AfterDays
        self._delivery = Delivery(after + days)

    def after_days(self):
        return self._delivery.AfterDays

Entity.register(Cargo)

if __name__ == '__main__':
    print 'Subclass:', issubclass(Cargo, Entity)
    print 'Instance:', isinstance(Cargo, Entity)
