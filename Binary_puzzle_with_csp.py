import copy


class Puzzle_csp:
    def __init__(self):
        self.puzzle = []
        self.degree = []
        self.backtrack_puzzles = []
        self.backtrack_degrees = []
        self.getting_input()
        self.zero_row = []
        self.one_row = []
        self.zero_column = []
        self.one_column = []

    def getting_input(self):
        nx, ny = input().split(' ')
        for i in range(int(nx)):
            row_string = input()
            self.puzzle.append(row_string.split(' '))
            row_string = row_string.replace('1', '')
            row_string = row_string.replace('0', '')
            row_string = row_string.replace('-', '01')
            self.degree.append(row_string.split(' '))
        print("self puzzle", self.puzzle)
        print("self degree", self.degree)


    def checking_equal_one_zero(sample_puzzle):
        for i in range(len(sample_puzzle)):
            column = [row[i] for row in sample_puzzle]
            if (sample_puzzle[i].count('1') != sample_puzzle[i].count('0')) or (column.count('1') != column.count('0')):
                return False
        return True

    def check_unique(self):
        # row
        for i in range(len(self.puzzle)):
            if not('-' in "".join(self.puzzle[i])):
                for j in range(i+1, len(self.puzzle)):
                    if ("".join(self.puzzle[i]) == "".join(self.puzzle[j])):
                        return False

        # column
        for i in range(len(self.puzzle)):
            column = [row[i] for row in self.puzzle]
            if not('-' in "".join(column)):
                for j in range(i+1, len(self.puzzle)):
                    column2 = [row[j] for row in self.puzzle]
                    if ("".join(column) == "".join(column2)):
                        return False

        return True

    def counting_one_zero(self):
        # counting number of zero and one in every column and row
        num = len(self.puzzle) // 2
        self.one_row = []
        self.one_column = []
        self.zero_row = []
        self.zero_column = []

        print("len self.puzzle", len(self.puzzle))
        for i in range(len(self.puzzle)):
            self.one_row.append(self.puzzle[i].count('1'))
            self.zero_row.append(self.puzzle[i].count('0'))
            column = [row[i] for row in self.puzzle]
            self.one_column.append(column.count('1'))
            self.zero_column.append(column.count('0'))

    def printing_puzzle(self):
        print("((((((((puzzle))))))))))")
        for i in self.puzzle:
            for j in i:
                print(j, end=',')
            print()
        print("((((((((degree))))))))))")
        for i in self.degree:
            for j in i:
                print(j, end=',')
            print()

    def check_possible(self):
        #counting number of zero and one in every column and row
        print("pppppppppp")
        self.printing_puzzle()
        num = len(self.puzzle)//2
        print("len self.puzzle", len(self.puzzle))
        for i in range(len(self.puzzle)):
            self.one_row.append(self.puzzle[i].count('1'))
            self.zero_row.append(self.puzzle[i].count('0'))
            column = [row[i] for row in self.puzzle]
            self.one_column.append(column.count('1'))
            self.zero_column.append(column.count('0'))

            if self.one_row[i] > num or self.zero_row[i] > num or self.one_column[i] > num or self.zero_column[i] > num:
                print("false pp")
                return False

        #row
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])-2):
                if (self.puzzle[i][j] == '0' and self.puzzle[i][j+1] == '0' and self.puzzle[i][j+2] == '0') or\
                        (self.puzzle[i][j] == '1' and self.puzzle[i][j+1] == '1' and self.puzzle[i][j+2] == '1'):
                    print("having 3 in row")
                    return False

        if len(self.puzzle[i]) > 4:
            for i in range(len(self.puzzle)):
                for j in range(len(self.puzzle[i])-4):
                    if (self.puzzle[i][j] == '0' and self.puzzle[i][j+1] == '0' and self.puzzle[i][j+2] == '-' and self.puzzle[i][j+3] == '1' and self.puzzle[i][j+4] == '1') or\
                            (self.puzzle[i][j] == '1' and self.puzzle[i][j+1] == '1' and self.puzzle[i][j+2] == '-' and self.puzzle[i][j+3] == '0' and self.puzzle[i][j+4] == '0'):
                        print("having 00-11 or 11-00 in row")
                        return False
        #column
        for i in range(len(self.puzzle)):
            column = [row[i] for row in self.puzzle]
            for j in range(len(column)-2):
                if (column[j] == '0' and column[j+1] == '0' and column[j+2] == '0') or\
                        (column[j] == '1' and column[j+1] == '1' and column[j+2] == '1'):
                    print("having 3 in column")
                    return False

        if len(self.puzzle[i]) > 4:
            for i in range(len(self.puzzle)):
                column = [row[i] for row in self.puzzle]
                for j in range(len(column)-4):
                    if (column[j] == '0' and column[j+1] == '0' and column[j+2] == '-' and column[j+3] == '1' and column[j+4] == '1') or\
                            (column[j] == '1' and column[j+1] == '1' and column[j+2] == '-' and column[j+3] == '0' and column[j+4] == '0'):
                        print("having 00-11 or 11-00 in column")
                        return False

        if Puzzle_csp.check_unique(self):
            return True
        else:
            return False

    def calculate_degree(self):
        print("calculate degree")
        Puzzle_csp.counting_one_zero(self)
        num = len(self.puzzle)//2
        #row
        for i in range(len(self.puzzle)):
            if self.one_row[i] == num:
                for j in range(len(self.puzzle[i])):
                    if self.puzzle[i][j]=='-':
                        self.degree[i][j]='0'
            if self.zero_row[i] == num:
                for j in range(len(self.puzzle[i])):
                    if self.puzzle[i][j] == '-':
                        self.degree[i][j] = '1'
        print("row checking", self.degree)

        #column
        for i in range(len(self.puzzle)):
            if self.one_column[i] == num:
                for j in range(len(self.puzzle)):
                    if self.puzzle[j][i] == '-':
                        self.degree[j][i] = '0'
            if self.zero_column[i] == num:
                for j in range(len(self.puzzle)):
                    if self.puzzle[j][i] == '-':
                        self.degree[j][i] = '1'
        print("column checking", self.degree)

        #row
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])-2):
                # 00- / 0-0 / -00
                if (self.puzzle[i][j] == '0' and self.puzzle[i][j+1] == '0' and self.puzzle[i][j+2] == '-'):
                    self.degree[i][j+2] = self.degree[i][j+2].replace('0', '')
                if (self.puzzle[i][j] == '0' and self.puzzle[i][j+1] == '-' and self.puzzle[i][j+2] == '0'):
                    self.degree[i][j+1] = self.degree[i][j+1].replace('0', '')
                if (self.puzzle[i][j] == '-' and self.puzzle[i][j+1] == '0' and self.puzzle[i][j+2] == '0'):
                    self.degree[i][j] = self.degree[i][j].replace('0', '')

                # 11- / 1-1 / -11
                if (self.puzzle[i][j] == '1' and self.puzzle[i][j+1] == '1' and self.puzzle[i][j+2] == '-'):
                    self.degree[i][j+2] = self.degree[i][j+2].replace('1', '')
                if (self.puzzle[i][j] == '1' and self.puzzle[i][j+1] == '-' and self.puzzle[i][j+2] == '1'):
                    self.degree[i][j+1] = self.degree[i][j+1].replace('1', '')
                if (self.puzzle[i][j] == '-' and self.puzzle[i][j+1] == '1' and self.puzzle[i][j+2] == '1'):
                    self.degree[i][j] = self.degree[i][j].replace('1', '')
        print("row repeat checking", self.degree)

        #column
        for i in range(len(self.puzzle)):
            column = [row[i] for row in self.puzzle]
            for j in range(len(self.puzzle[i])-2):
                # 00- / 0-0 / -00
                if (column[j] == '0' and column[j+1] == '0' and column[j+2] == '-'):
                    self.degree[j+2][i] = self.degree[j+2][i].replace('0', '')
                if (column[j] == '0' and column[j+1] == '-' and column[j+2] == '0'):
                    self.degree[j+1][i] = self.degree[j+1][i].replace('0', '')
                if (column[j] == '-' and column[j+1] == '0' and column[j+2] == '0'):
                    self.degree[j][i] = self.degree[j][i].replace('0', '')

                # 11- / 1-1 / -11
                if (column[j] == '1' and column[j+1] == '1' and column[j+2] == '-'):
                    self.degree[j+2][i] = self.degree[j+2][i].replace('1', '')
                if (column[j] == '1' and column[j+1] == '-' and column[j+2] == '1'):
                    self.degree[j+1][i] = self.degree[j+1][i].replace('1', '')
                if (column[j] == '-' and column[j+1] == '1' and column[j+2] == '1'):
                    self.degree[j][i] = self.degree[j][i].replace('1', '')
        print("column repeat checking", self.degree)

    def puzzle_solved(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if '-' in self.puzzle[i][j]:
                    return False
        return True

    def random_choosing(self):
        # store previous self.degree for backtracking
        self.backtrack_puzzles.append(copy.deepcopy(self.puzzle))
        self.backtrack_degrees.append(copy.deepcopy(self.degree))

        # random choosing
        fine = False
        for i in range(len(self.degree)):
            for j in range(len(self.degree)):
                if len(self.degree[i][j])==2:
                    self.degree[i][j] = self.degree[i][j].replace('1', '')
                    print("random", i, j)
                    fine = True
                    break
            if fine:
                break

    def reverse_MRV(self):
        print("len backtrack_puzzles", len(self.backtrack_puzzles))
        self.puzzle = self.backtrack_puzzles[-1]
        self.degree = self.backtrack_degrees[-1]
        self.backtrack_degrees.pop()
        self.backtrack_puzzles.pop()
        print("len backtrack_puzzles after pop", len(self.backtrack_puzzles))

        fine = False
        for i in range(len(self.degree)):
            for j in range(len(self.degree)):
                if len(self.degree[i][j])==2:
                    self.degree[i][j] = self.degree[i][j].replace('0', '')
                    print("random backtrack", i, j)
                    fine = True
                    break
            if fine:
                break

    def MRV_heuristic(self):
        pre_puzzle = copy.deepcopy(self.puzzle)
        print("pre_puzzle", pre_puzzle)
        print("pre_degree", self.degree)
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if len(self.degree[i][j]) == 1:
                    self.puzzle[i][j] = self.degree[i][j]
                    self.degree[i][j] = self.degree[i][j].replace(self.puzzle[i][j], '')
                    self.calculate_degree()
                    return False

        print("after MRV", self.puzzle)
        print("self_degree", self.degree)
        print("check_similar", self.check_similar(pre_puzzle))
        #print("pre_puzzle", pre_puzzle)
        #return self.check_similar(pre_puzzle)
        return True

    def check_similar(self, pre_puzzle):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[j][i] != pre_puzzle[j][i]:
                    return False
        return True

    def check_still_possible(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == '-' and len(self.degree[i][j]) == 0:
                    return False
        return True

    def calling_methods(self):
        self.check_possible()
        self.calculate_degree()

        while True:
            # fill the certain cells
            while not(self.MRV_heuristic()):
                #self.calculate_degree()
                if not (self.check_still_possible()) and len(self.backtrack_puzzles) > 0:
                    self.reverse_MRV()

            # if there is still any - in puzzle
            if not(self.puzzle_solved()):
                self.random_choosing()
                self.calculate_degree()

            else:
                if self.check_unique():
                    print("puzzle solved")
                    break
                else:
                    # backtrack if we had random_choosing
                    if len(self.backtrack_puzzles) > 0:
                        self.reverse_MRV()
                    else:
                        print("not possible because we have non unique row or column")
                        break

            # check if the puzzle still can have an answer
            if not(self.check_still_possible()):
                print("not possible")
                break

puzzle_csp = Puzzle_csp()
puzzle_csp.calling_methods()
