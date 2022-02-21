import numpy as np

testcase = [
    [True, False, True],
    [True, False, True],
    [False, True, False],
    [True, False, True],
]


def transpose(array):
    return np.array(array).T.tolist()


class Game:
    @staticmethod
    def load_line(line):
        if not "__iter__" in dir(line):
            raise Exception("line is not iterable")
        output = []
        counter = 0
        for x in line:
            if x:
                counter += 1
            else:
                if counter:  # append if not zero
                    output.append(counter)
                    counter = 0
        if counter:
            output.append(counter)
        return tuple(output)

    def load_from_list_of_lists(self, list_of_lists):
        if not "__iter__" in dir(list_of_lists):
            raise Exception("list_of_lists is not iterable")
        # todo check if it's rectangular
        self.game_raw = list_of_lists
        transposed = transpose(self.game_raw)
        self.rows = [self.load_line(x) for x in self.game_raw]
        self.columns = [self.load_line(x) for x in transposed]
        return self

    def solve_from_rows_and_columns(self):
        if not self.rows or not self.columns:
            raise Exception("Rows and columns are not calculated yet. Supply data first.")
        self.solution = Game()
        self.solution.game_raw = [[None] * len(self.columns)] * len(self.rows)

        # get all possibilities and make an AND out of them
        for index, row in enumerate(self.rows):
            outcome = self.calculate_and_AND_all_possibilites(
                row_in_question=self.solution.game_raw[index],
                row_values=row
            )
            self.solution.game_raw[index] = outcome

    def calculate_and_AND_all_possibilites(self, row_in_question, row_values):
        one_configuration = []
        for number in row_values:
            one_configuration = one_configuration + [False] + [True] * row_values[number]
        return

game = Game().load_from_list_of_lists(
    testcase
)
game.solve_from_rows_and_columns()
