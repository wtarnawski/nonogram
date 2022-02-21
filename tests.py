import unittest
from main import Game

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()

    def test_process_line(self):
        self.assertEqual(
            Game.load_line(
                [1,1,1,1,0,0,0,1,0,1,1,1,0,0]
            ),
            (4,1,3)
        )
        self.assertEqual(
            Game.load_line(
                [0]*80 + [1]*7 + [0]*3 + [1]
            ),
            (7,1)
        )
        self.assertEqual(
            Game.load_line(
                [1,0,1,0,1,0,1]
            ),
            (1,1,1,1)
        )
    # def test_load_data_into_dataframe(self):
    #     self.assertEqual(
    #         [
    #             [True, False, True],
    #             [True, False, True],
    #             [False, True, False]
    #         ],
    #     )
    # def test_something(self):
    #     self.assertEqual(True, False)
    def test_loading_data(self):
        testcase = [
            [True, False, True],
            [True, False, True],
            [False, True, False],
            [True, False, True],
        ]
        self.game.load_from_list_of_lists(
            testcase
        )
        self.assertEqual(
            self.game.rows,
            [(1, 1), (1, 1), (1,), (1, 1)]
        )
        self.assertEqual(
            self.game.columns,
            [(2, 1), (1,), (2, 1)]
        )


if __name__ == '__main__':
    unittest.main()
