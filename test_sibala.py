import unittest

from sibala import Sibala


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sibala = Sibala()

    # Input: "Amy:2 2 6 6  Lin:6 6 3 1"
    # Output: "Amy wins, normal point: '12'"
    def test_amy_win_normal_point(self):
        input_str = "Amy:2 2 6 6  Lin:6 6 3 1"
        expected = "Amy wins. normal point: 12"
        self.assertEqual(expected, self.sibala.get_sibala(input_str))

    # Input: "Amy:1 2 3 4  Lin:6 6 1 2"
    # Output: "Lin wins. normal point: 3"
    def test_lin_win_normal_point(self):
        input_str = "Amy:1 2 3 4  Lin:6 6 1 2"
        expected = "Lin wins. normal point: 3"
        self.assertEqual(expected, self.sibala.get_sibala(input_str))


    # Input: "Amy:2 2 6 6  Lin:2 6 6 2"
    # Output: "Tie."
    def test_tie_normal_point(self):
        input_str = "Amy:2 2 6 6  Lin:2 6 6 2"
        expected = "Tie."
        self.assertEqual(expected, self.sibala.get_sibala(input_str))

    # Input: "Amy:1 1 1 1  Lin:3 3 3 3"
    # Output: "Lin wins. all the same kind 3"
    def test_lin_wins_all_the_same_kind(self):
        input_str = "Amy:1 1 1 1  Lin:3 3 3 3"
        expected = "Lin wins. all the same kind: 3"
        self.assertEqual(expected, self.sibala.get_sibala(input_str))

    # Input: "Amy:1 1 3 3  Lin:1 1 4 2"
    # Output: "Lin wins. normal point: 4"
    def test_lin_wins_normal_point_with_same_score(self):
        input_str = "Amy:1 1 3 3  Lin:1 1 4 2"
        expected = "Lin wins. normal point: 4"
        self.assertEqual(expected, self.sibala.get_sibala(input_str))

    # Input: "Amy:6 6 6 6  Lin:3 3 3 3"
    # Output: "Amy wins. all the same kind: 6"
    def test_amy_wins_both_all_the_same_kind(self):
        input_str = "Amy:6 6 6 6  Lin:3 3 3 3"
        expected = "Amy wins. all the same kind: 6"
        self.assertEqual(expected, self.sibala.get_sibala(input_str))

    # Input: "Amy:6 6 6 6  Lin:6 6 6 6"
    # Output: "Tie."
    def test_tie_both_all_the_same_kind(self):
        input_str = "Amy:6 6 6 6  Lin:6 6 6 6"
        expected = "Tie."
        self.assertEqual(expected, self.sibala.get_sibala(input_str))

    # Input: "Amy:6 6 6 1  Lin:1 2 3 4"
    # Output: "Tie."
    def test_tie_both_no_points(self):
        input_str = "Amy:6 6 6 1  Lin:1 2 3 4"
        expected = "Tie."
        self.assertEqual(expected, self.sibala.get_sibala(input_str))

if __name__ == '__main__':
    unittest.main()
