import copy

import Binary_puzzle_with_csp as csp

class Puzzle_csp:
    def __init__(self):
        self.puzzle = []
        self.degree = []
        self.backtrack_puzzles = []
        self.backtrack_degrees = []
        csp.Puzzle_csp.getting_input(self)
        self.zero_row = []
        self.one_row = []
        self.zero_column = []
        self.one_column = []
        #self.mac_degree = []

    """
    def updating_mac_degree(self, i, j):
        column = [row[j] for row in self.puzzle]
        self.mac_degree[i][j] = int("".join(self.puzzle[i]).count('-') - 1) + int("".join(column).count('-') - 1)
    """
    """   
    def calculating_mac_degree(self):
        for i in range(len(self.puzzle)):
            degree_list = []
            for j in range(len(self.puzzle)):
                column = [row[i] for row in self.puzzle]
                if self.puzzle[i][j]=='-':
                    degree_list.append(int("".join(self.puzzle[i]).count('-')-1) + int("".join(column).count('-')-1))
                else:
                    degree_list.append(0)
            self.mac_degree.append(degree_list)
    """

    def updating_degrees(self, x, y):
        print("updating_degrees")
        queue_ = self.find_neighbors(x, y)
        print("neighbors", queue_)
        while len(queue_) > 0:
            print("quew", queue_, queue_[0][0])
            changed = self.update_cell_degree(queue_[0][0], queue_[0][1])
            print("changed, x, y: ", changed, x, y)
            current_cell = queue_.pop(0)
            if changed:
                new_neighbors = self.find_neighbors(current_cell[0], current_cell[1])
                for i in new_neighbors:
                    queue_.append(i)

    def update_cell_degree(self, x, y):
        pre_degree = copy.deepcopy(self.degree[x][y])
        print("before updating", self.degree)

        csp.Puzzle_csp.counting_one_zero(self)
        num = len(self.puzzle)//2

        #row
        if self.one_row[x] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        if self.zero_row[x] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        print("row updating", self.degree)

        #column
        if self.one_column[y] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('1', '')
        if self.zero_column[y] == num:
            if self.puzzle[x][y] == '-':
                self.degree[x][y] = self.degree[x][y].replace('0', '')
        print("column updating", self.degree)

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
        print("column repeat updating", self.degree)

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
        print("row repeat updating", self.degree)

        if pre_degree == self.degree[x][y]:
            return False
        else:
            return True

    def find_neighbors(self, x, y):
        print("find_neighbors")
        neighbors = []
        row = self.puzzle[x]
        column = [row[y] for row in self.puzzle]
        print("______________________________________________")
        print("column", column)
        for j in range(len(row)):
            print("row", row[j], end=' ')
            if row[j]=='-' and j!=y:
                neighbors.append([x, j])
        for i in range(len(row)):
            if column[i]=='-' and i!=x:
                neighbors.append([i, y])
        print("len neighbors", len(neighbors))
        print("neighbors in function", neighbors)
        return neighbors

    def MRV_heuristic(self):
        pre_puzzle = copy.deepcopy(self.puzzle)
        print("pre_puzzle", pre_puzzle)
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle)):
                if len(self.degree[i][j]) == 1:
                    self.puzzle[i][j] = self.degree[i][j]
                    self.degree[i][j] = self.degree[i][j].replace(self.puzzle[i][j], '')
                    self.updating_degrees(i, j)
                    print("residam be updating_degrees")
                    return False
        print("after first MRV", self.puzzle)

        # print("pre_puzzle", pre_puzzle)
        print("self_puzzle", self.puzzle)
        print("self_degree", self.degree)
        return True

    def calling_method(self):
        csp.Puzzle_csp.check_possible(self)
        csp.Puzzle_csp.calculate_degree(self)

        #self.calculating_mac_degree()
        while True:
            if self.MRV_heuristic():
                break
            else:
                pass


puzzle_csp = Puzzle_csp()
puzzle_csp.calling_method()