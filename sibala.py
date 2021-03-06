from dataclasses import dataclass
from enum import IntEnum
import collections


class DiceCategory(IntEnum):
    NO_POINTS = 0
    NORMAL_POINT = 1
    ALL_THE_SAME_KIND = 2


category_to_str_dict = {
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

    def __eq__(self, other):
        return (self.score, self.max_valid_dice) == (other.score, other.max_valid_dice)


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

    def _get_output(self) -> Output:
        c = collections.Counter(self.dices)
        if (n := len(c.keys())) == 1:
            return Output(self.dices[0], 0)
        elif n == 4:
            return Output(0, 0)
        elif n == 3:
            # case: 6, 6, 1, 2
            score, max_valid_dice = 0, 0
            for k, v in c.items():
                if v == 2:
                    continue
                score += k
                max_valid_dice = max(max_valid_dice, k)
            return Output(score, max_valid_dice)
        else: # n= 2
            if set(c.values()) == set([1, 3]):
                return Output(0, 0)
            # case: 6, 6, 2, 2
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


class Sibala(object):
    def _parse_player_info(self, input_str: str):
        p1, p2 = input_str.split('  ')
        p1_name, p1_dice_str = p1.split(':')
        p2_name, p2_dice_str = p2.split(':')

        p1_obj = Player(p1_name, [int(num) for num in p1_dice_str.split(' ')])
        p2_obj = Player(p2_name, [int(num) for num in p2_dice_str.split(' ')])

        return p1_obj, p2_obj

    def get_winner(self, p1: Player, p2: Player) -> tuple[Player, int]:
        winner = None
        output = None
        if p1.category_type != p2.category_type:
            winner = p1 if p1.category_type > p2.category_type else p2
            output = winner.output.score
        elif p1.category_type == DiceCategory.ALL_THE_SAME_KIND:
            if p1.output != p2.output:
                winner = p1 if p1.output > p2.output else p2
                output = winner.output.score
        elif p1.category_type == DiceCategory.NORMAL_POINT:
            if p1.output != p2.output:
                winner = p1 if p1.output > p2.output else p2
                output = winner.output.score if p1.output.score != p2.output.score else winner.output.max_valid_dice

        return winner, output

    # entry point
    def get_sibala_result(self, input_str: str):
        p1_obj, p2_obj = self._parse_player_info(input_str)
        winner, output = self.get_winner(p1_obj, p2_obj)
        if winner:
            return f"{winner.name} wins. {category_to_str_dict[winner.category_type]}: {output}"
        return "Tie."
