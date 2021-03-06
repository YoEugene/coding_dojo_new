from dataclasses import dataclass




@dataclass
class Player(object):
    name: str
    dices: list[int]
    category_type = _get_category(self.dices)
    def __cmp__(self, other):
        pass

    def _get_category(dices):
        pass


class Sibala(object):
    def _parse(self, input_str):
        return
    def get_sibala(self, input):
