import copy

#import Binary_puzzle_with_csp as csp

class Puzzle_csp:
    def __init__(self):
        self.puzzle = []
        self.degree = []
        self.backtrack_puzzles = []
        self.backtrack_degrees = []
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

    def printing_puzzle(self):
        for i in self.puzzle:
            for j in i:
                print(j, end=' ')
            print()

    def check_possible(self):
        #counting number of zero and one in every column and row
        num = len(self.puzzle)//2
        # print("len self.puzzle", len(self.puzzle))
        for i in range(len(self.puzzle)):
            self.one_row.append(self.puzzle[i].count('1'))
            self.zero_row.append(self.puzzle[i].count('0'))
            column = [row[i] for row in self.puzzle]
            self.one_column.append(column.count('1'))
            self.zero_column.append(column.count('0'))

            if self.one_row[i] > num or self.zero_row[i] > num or self.one_column[i] > num or self.zero_column[i] > num:
                return False

        #row
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])-2):
                if (self.puzzle[i][j] == '0' and self.puzzle[i][j+1] == '0' and self.puzzle[i][j+2] == '0') or\
                        (self.puzzle[i][j] == '1' and self.puzzle[i][j+1] == '1' and self.puzzle[i][j+2] == '1'):
                    # print("having 3 in row")
                    return False

        if len(self.puzzle[i]) > 4:
            for i in range(len(self.puzzle)):
                for j in range(len(self.puzzle[i])-4):
                    if (self.puzzle[i][j] == '0' and self.puzzle[i][j+1] == '0' and self.puzzle[i][j+2] == '-' and self.puzzle[i][j+3] == '1' and self.puzzle[i][j+4] == '1') or\
                            (self.puzzle[i][j] == '1' and self.puzzle[i][j+1] == '1' and self.puzzle[i][j+2] == '-' and self.puzzle[i][j+3] == '0' and self.puzzle[i][j+4] == '0'):
                        # print("having 00-11 or 11-00 in row")
                        return False
        #column
        for i in range(len(self.puzzle)):
            column = [row[i] for row in self.puzzle]
            for j in range(len(column)-2):
                if (column[j] == '0' and column[j+1] == '0' and column[j+2] == '0') or\
                        (column[j] == '1' and column[j+1] == '1' and column[j+2] == '1'):
                    # print("having 3 in column")
                    return False

        if len(self.puzzle[i]) > 4:
            for i in range(len(self.puzzle)):
                column = [row[i] for row in self.puzzle]
                for j in range(len(column)-4):
                    if (column[j] == '0' and column[j+1] == '0' and column[j+2] == '-' and column[j+3] == '1' and column[j+4] == '1') or\
                            (column[j] == '1' and column[j+1] == '1' and column[j+2] == '-' and column[j+3] == '0' and column[j+4] == '0'):
                        # print("having 00-11 or 11-00 in column")
                        return False

        if self.check_unique():
            return True
        else:
            return False

    def check_still_possible(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if self.puzzle[i][j] == '-' and len(self.degree[i][j]) == 0:
                    return False
        return True

    def counting_one_zero(self):
        # counting number of zero and one in every column and row
        num = len(self.puzzle) // 2
        self.one_row = []
        self.one_column = []
        self.zero_row = []
        self.zero_column = []

        for i in range(len(self.puzzle)):
            self.one_row.append(self.puzzle[i].count('1'))
            self.zero_row.append(self.puzzle[i].count('0'))
            column = [row[i] for row in self.puzzle]
            self.one_column.append(column.count('1'))
            self.zero_column.append(column.count('0'))

    def calculate_degree(self):
        self.counting_one_zero()
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

    def updating_degrees(self, x, y):
        queue_ = self.find_neighbors(x, y)
        while len(queue_) > 0:
            changed = self.update_cell_degree(queue_[0][0], queue_[0][1])
            current_cell = queue_.pop(0)
            """
            if changed:
                new_neighbors = self.find_neighbors(current_cell[0], current_cell[1])
                for i in new_neighbors:
                    queue_.append(i)
            """

    def update_cell_degree(self, x, y):
        pre_degree = copy.deepcopy(self.degree[x][y])

        self.counting_one_zero()
        num = len(self.puzzle)//2

        #row
        if self.one_row[x] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        if self.zero_row[x] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('0', '')

        #column
        if self.one_column[y] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        if self.zero_column[y] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('0', '')

        #column
        # 00-
        if y > 1:
            if (self.puzzle[x][y-2] == '0' and self.puzzle[x][y-1] == '0' and self.puzzle[x][y] == '-'):
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        # 0-0
        if y > 0 and y < len(self.puzzle) - 1:
            if (self.puzzle[x][y-1] == '0' and self.puzzle[x][y] == '-' and self.puzzle[x][y+1] == '0'):
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        # -00
        if y < len(self.puzzle) - 2:
            if (self.puzzle[x][y] == '-' and self.puzzle[x][y+1] == '0' and self.puzzle[x][y+2] == '0'):
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        # 11-
        if y > 1:
            if (self.puzzle[x][y-2] == '1' and self.puzzle[x][y-1] == '1' and self.puzzle[x][y] == '-'):
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        # 1-1
        if y > 0 and y < len(self.puzzle) - 1:
            if (self.puzzle[x][y-1] == '1' and self.puzzle[x][y] == '-' and self.puzzle[x][y+1] == '1'):
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        # -11
        if y < len(self.puzzle) - 2:
            if (self.puzzle[x][y] == '-' and self.puzzle[x][y+1] == '1' and self.puzzle[x][y+2] == '1'):
                self.degree[x][y] = self.degree[x][y].replace('1', '')

        #row
        # 00-
        if x > 1:
            if (self.puzzle[x-2][y] == '0' and self.puzzle[x-1][y] == '0' and self.puzzle[x][y] == '-'):
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        # 0-0
        if x > 0 and x < len(self.puzzle) - 1:
            if (self.puzzle[x-1][y] == '0' and self.puzzle[x][y] == '-' and self.puzzle[x+1][y] == '0'):
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        # -00
        if x < len(self.puzzle) - 2:
            if (self.puzzle[x][y] == '-' and self.puzzle[x+1][y] == '0' and self.puzzle[x+2][y] == '0'):
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        # 11-
        if x > 1:
            if (self.puzzle[x-2][y] == '1' and self.puzzle[x-1][y] == '1' and self.puzzle[x][y] == '-'):
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        # 1-1
        if x > 0 and x < len(self.puzzle) - 1:
            if (self.puzzle[x-1][y] == '1' and self.puzzle[x][y] == '-' and self.puzzle[x+1][y] == '1'):
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        # -11
        if x < len(self.puzzle) - 2:
            if (self.puzzle[x][y] == '-' and self.puzzle[x+1][y] == '1' and self.puzzle[x+2][y] == '1'):
                self.degree[x][y] = self.degree[x][y].replace('1', '')

        if pre_degree == self.degree[x][y]:
            return False
        else:
            return True

    def find_neighbors(self, x, y):
        neighbors = []
        row = self.puzzle[x]
        column = [row[y] for row in self.puzzle]
        for j in range(len(row)):
            if row[j]=='-' and j!=y:
                neighbors.append([x, j])
        for i in range(len(row)):
            if column[i]=='-' and i!=x:
                neighbors.append([i, y])
        return neighbors

    def MRV_heuristic(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if len(self.degree[i][j]) == 1:
                    self.puzzle[i][j] = self.degree[i][j]
                    self.degree[i][j] = self.degree[i][j].replace(self.puzzle[i][j], '')
                    self.updating_degrees(i, j)
                    return False
        return True

    def reverse_MRV(self):
        self.puzzle = self.backtrack_puzzles[-1]
        self.degree = self.backtrack_degrees[-1]
        self.backtrack_degrees.pop()
        self.backtrack_puzzles.pop()

        fine = False
        for i in range(len(self.degree)):
            for j in range(len(self.degree)):
                if len(self.degree[i][j])==2:
                    self.degree[i][j] = self.degree[i][j].replace('0', '')
                    fine = True
                    break
            if fine:
                break

    def random_choosing(self):
        # print("----------random_choosing----------")
        # store previous self.degree for backtracking
        self.backtrack_puzzles.append(copy.deepcopy(self.puzzle))
        self.backtrack_degrees.append(copy.deepcopy(self.degree))

        # random choosing
        fine = False
        for i in range(len(self.degree)):
            for j in range(len(self.degree)):
                if len(self.degree[i][j]) == 2:
                    self.degree[i][j] = self.degree[i][j].replace('1', '')
                    fine = True
                    break
            if fine:
                break

    def check_unique(self):
        # row
        for i in range(len(self.puzzle)):
            if not('-' in "".join(self.puzzle[i])):
                for j in range(i+1, len(self.puzzle)):
                    if ("".join(self.puzzle[i]) == "".join(self.puzzle[j])):
                        # print("check_unique row i, j: ", i, j)
                        return False

        # column
        for i in range(len(self.puzzle)):
            column = [row[i] for row in self.puzzle]
            if not('-' in "".join(column)):
                for j in range(i+1, len(self.puzzle)):
                    column2 = [row[j] for row in self.puzzle]
                    if ("".join(column) == "".join(column2)):
                        # print("check_unique column i, j: ", i, j)
                        return False

        return True

    def puzzle_solved(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if '-' in self.puzzle[i][j]:
                    return False
        return True

    def calling_method(self):
        self.getting_input()
        # self.printing_puzzle()
        self.check_possible()
        self.calculate_degree()
        #self.counting_one_zero()

        while True:
            while not (self.MRV_heuristic()):
                #if self.MRV_heuristic():
                if not (self.check_still_possible()) and len(self.backtrack_puzzles) > 0:
                    self.reverse_MRV()
                #break

            if not (self.puzzle_solved()):
                self.random_choosing()
                if not (self.check_possible()) and len(self.backtrack_puzzles) > 0:
                    self.reverse_MRV()
            else:
                if self.check_unique():
                    # print("puzzle solved")
                    self.printing_puzzle()
                    break
                else:
                    # backtrack if we had random_choosing
                    if len(self.backtrack_puzzles) > 0:
                        self.reverse_MRV()
                    else:
                        print("not possible because we have non unique row or column")
                        break
            if not(self.check_still_possible()):
                self.printing_puzzle()
                print("not possible")
                break


puzzle_csp = Puzzle_csp()
puzzle_csp.calling_method()