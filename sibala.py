from dataclasses import dataclass
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


@dataclass
class Output(object):
    score: int  # if 6 6 2 3 => 5, 6 6 1 4 => 5
    max_valid_dice: int  # if 6 6 2 3 => 3, 6 6 1 4 => 4

    def __gt__(self, other):
        return (self.score, self.max_valid_dice) > (other.score, other.max_valid_dice)


class Player(object):
    name: str
    dices: list[int]
    score: int
    max_dice: int
    category_type: DiceCategory
    output: Output

    def __init__(self, name: str, dices: list[int]):
        self.name = name
        self.dices = dices
        self.category_type = self._get_category()
        self.output = self._get_output()

    def __repr__(self):
        return f"{self.name=}, {self.dices=}, {self.category_type=}, {self.output=}"

    def _get_output(self):
        c = collections.Counter(self.dices)
        if (n := len(c.keys())) == 1:
            return Output(self.dices[0], 0)
        elif n == 4:
            return Output(0, 0)
        elif n == 3:
            # 6, 6, 1, 2
            res_s, res_m = 0, 0
            for k, v in c.items():
                if v == 2:
                    continue
                res_s += k
                res_m = max(res_m, k)
            return Output(res_s, res_m)
        else:
            if set(c.values()) == set([1, 3]):
                return Output(0, 0)
            # 6, 6, 2, 2
            return Output(max(c.keys()) * 2, 0)

    def _get_category(self) -> DiceCategory:
        c = collections.Counter(self.dices)
        if (n := len(c.keys())) == 1:
            return DiceCategory.ALL_THE_SAME_KIND
        elif n == 4:
            return DiceCategory.NO_POINTS
        elif n == 2:
            if set(c.values()) == set([1, 3]):
                return DiceCategory.NO_POINTS
        return DiceCategory.NORMAL_POINT


def get_winner(p1: Player, p2: Player) -> tuple[bool, Player, int]:
    if p1.category_type != p2.category_type:
        winner = p1 if p1.category_type > p2.category_type else p2
        return True, winner, winner.output.score
    if p1.category_type == DiceCategory.ALL_THE_SAME_KIND:
        if p1.output != p2.output:
            winner = p1 if p1.output > p2.output else p2
            return True, winner, winner.output.score
        return False, None, None
    elif p1.category_type == DiceCategory.NORMAL_POINT:
        if p1.output != p2.output:
            winner = p1 if p1.output > p2.output else p2
            return True, winner, winner.output.score if p1.output.score != p2.output.score else winner.output.max_valid_dice

    return False, None, None


class Sibala(object):
    def _parse(self, input_str: str):
        p1, p2 = input_str.split('  ')
        p1_name, p1_dice_str = p1.split(':')
        p2_name, p2_dice_str = p2.split(':')

        p1_obj = Player(p1_name, [int(num) for num in p1_dice_str.split(' ')])
        p2_obj = Player(p2_name, [int(num) for num in p2_dice_str.split(' ')])

        return p1_obj, p2_obj

    # entry point
    def get_sibala(self, input_str: str):
        p1_obj, p2_obj = self._parse(input_str)
        has_winner, winner, output = get_winner(p1_obj, p2_obj)
        if has_winner:
            return f"{winner.name} wins. {category_dict[winner.category_type]}: {output}"
        return "Tie."
