from enum import IntEnum
import collections


class DiceCategory(IntEnum):
    NO_POINTS = 0
    NORMAL_POINT = 1
    ALL_THE_SAME_KIND = 2


category_dict = {
    DiceCategory.NO_POINTS: 'no points',
    DiceCategory.NORMAL_POINT: 'normal point',
    DiceCategory.ALL_THE_SAME_KIND: 'all the same kind'
}


class Player(object):
    name: str
    dices: list[int]
    category_type: DiceCategory
    output: tuple[int, int]

    def __init__(self, name: str, dices: list[int]):
        self.name = name
        self.dices = dices
        self.category_type = self._get_category(self.dices)
        self.output = self._get_output()

    def __repr__(self):
        return f"{self.name=}, {self.dices=}, {self.category_type=}, {self.output=}"

    def _get_output(self):
        c = collections.Counter(self.dices)
        if (n := len(c.keys())) == 1:
            return self.dices[0], 0
        elif n == 4:
            return 0, 0
        elif n == 3:
            # 6, 6, 1, 2
            res_s, res_m = 0, 0
            for k, v in c.items():
                if v == 2:
                    continue
                res_s += k
                res_m = max(res_m, k)
            return res_s, res_m
        else:
            if set(c.values()) == set([1, 3]):
                return 0, 0
            # 6, 6, 2, 2
            return max(c.keys()) * 2, 0


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


def get_winner(p1: Player, p2: Player) -> tuple[bool, Player, int]:
    if p1.category_type != p2.category_type:
        winner = p1 if p1.category_type > p2.category_type else p2
        return True, winner, winner.output[0]
    if p1.category_type == DiceCategory.ALL_THE_SAME_KIND:
        winner = p1 if p1.category_type > p2.category_type else p2
        return True, winner, winner.output[0]
    elif p1.category_type == DiceCategory.NORMAL_POINT:
        if p1.output != p2.output:
            winner = p1 if p1.output > p2.output else p2
            return True, winner, winner.output[0] if p1.output[0] != p2.output[0] else winner.output[1]

    return False, None, None



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

        has_winner, winner, output = get_winner(p1_obj, p2_obj)

        if has_winner:
            return f"{winner.name} wins. {category_dict[winner.category_type]}: {output}"

        return "Tie."





