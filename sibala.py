from enum import Enum
import collections


class DiceCategory(Enum):
    NO_POINTS = 0
    NORMAL_POINT = 1
    ALL_THE_SAME_KIND = 2



class Player(object):
    name: str
    dices: list[int]
    category_type: DiceCategory
    output: int

    def __init__(self, name: str, dices: list[int]):
        self.name = name
        self.dices = dices
        self.category_type = self._get_category(self.dices)
        self.output = self._get_output()

    def __repr__(self):
        return f"{self.name=}, {self.dices=}, {self.category_type=}"

    def _get_output(self):
        return 0

    def _get_category(self, dices: list[int]) -> DiceCategory:
        c = collections.Counter(dices)
        if (n := len(c.keys())) == 1:
            return DiceCategory.ALL_THE_SAME_KIND
        elif n == 4:
            return DiceCategory.NO_POINTS
        elif n == 2:
            if set(c.values()) == set([1, 3]):
                return DiceCategory.NO_POINTS
        return DiceCategory.NORMAL_POINT

    def __cmp__(self, other):
        pass




class Sibala(object):
    @staticmethod
    def _parse(input_str: str):
        p1, p2 = input_str.split('  ')
        p1_name, p1_dice_str = p1.split(':')
        p2_name, p2_dice_str = p2.split(':')

        p1_obj = Player(p1_name, [int(num) for num in p1_dice_str.split(' ')])
        p2_obj = Player(p2_name, [int(num) for num in p2_dice_str.split(' ')])

        return p1_obj, p2_obj

    @staticmethod
    def get_sibala(input_str: str):
        p1_obj, p2_obj = Sibala._parse(input_str)
        print(p1_obj, p2_obj)

        if p1_obj != p2_obj:
            if xxxx:
                return f"{winner_obj.name} wins. {winner_obj.category_type}: '{winner_obj.output}'"
            winner_obj = p1_obj if p1_obj > p2_obj else p2_obj
            return f"{winner_obj.name} wins. {winner_obj.category_type}: '{winner_obj.output}'"
        return "Tie."




