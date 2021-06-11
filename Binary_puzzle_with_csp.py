class Puzzle_csp:
    def __init__(self):
        self.puzzle = self.getting_input()

    @staticmethod
    def getting_input():
        nx, ny = input().split(' ')
        puzzle = []
        for i in range(int(nx)):
            puzzle.append(input().split(' '))
        return puzzle

    @staticmethod
    def checking_equal_one_zero(sample_puzzle):
        for i in range(len(sample_puzzle)):
            column = [row[i] for row in sample_puzzle]
            if (sample_puzzle[i].count('1') != sample_puzzle[i].count('0')) or (column.count('1') != column.count('0')):
                return False
        return True


puzzle_csp = Puzzle_csp()
puzzle_csp.checking_equal_one_zero()
