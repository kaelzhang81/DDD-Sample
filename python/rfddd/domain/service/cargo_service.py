# coding=utf-8
"""the implement of entity"""


from .delivery import Delivery
from domain.model import ceargo

class CargoService(object):
    def __init__(self, cargo_repo, cargo_provider):
        self._cargo_repo = cargo_repo
        self._cargo_provider = cargo_provider

    def create(self, id, days):
        delivery = Delivery(days);
        cargo = Cargo(delivery, id);
        self._cargo_repo.save(cargo);
        self._cargo_provider.confirm(cargo);

    def delay(self, id, days):
        cargo = self._cargo_repo.find_by_id(id);
        if cargo is not None:
            cargo.Delay(days);
            self._cargo_repo.save(cargo);
            self._cargo_provider.confirm(cargo);
