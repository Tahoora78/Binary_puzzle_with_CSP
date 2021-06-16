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

    def updating_after_first_change(self, x, y):
        neighbors_row, neighbors_column = self.find_neighbors(x, y)
        for i,j in neighbors_row:
            pass

    def updating_after_degree_updated(self):


    def find_neighbors(self, x, y):
        neighbors_row = []
        neighbors_column = []
        row = self.puzzle[x]
        column = [row[y] for row in self.puzzle]
        for i in range(len(row)):
            if row[i]=='-' and i!=x:
                neighbors_row.append([i, y])
        for j in range(len(column)):
            if column[j]=='-' and j!=y:
                neighbors_column.append([x, j])
        return neighbors_row, neighbors_column

    def MRV_heuristic(self):
        pre_puzzle = copy.deepcopy(self.puzzle)
        print("pre_puzzle", pre_puzzle)
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if len(self.degree[i][j]) == 1:
                    self.puzzle[i][j] = self.degree[i][j]
                    self.degree[i][j] = self.degree[i][j].replace(self.puzzle[i][j], '')
                    self.updating_degree(i, j)
                    return False
        print("after first MRV", self.puzzle)

        # print("pre_puzzle", pre_puzzle)
        print("self_puzzle", self.puzzle)
        return True

    def calling_method(self):
        csp.Puzzle_csp.check_possible()
        #self.calculating_mac_degree()
        while True:
            if self.MRV_heuristic():
                break
            else:


puzzle_csp = Puzzle_csp()
puzzle_csp.calling_method()