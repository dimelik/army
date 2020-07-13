from soldier import Soldier


class SoldierBuilder:

    def __init__(self, military_unit_number, name) -> None:
        self.reset(self, military_unit_number, name)

    def reset(self, military_unit_number, name) -> None:
        self._product = Soldier(self, military_unit_number, name)

    @property
    def product(self) -> Soldier:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")