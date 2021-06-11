class Puzzle_csp:
    def __init__(self):
        self.puzzle = []
        self.degree = []
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
        pass

    def check_possible(self):
        #counting number of zero and one in every column and row
        num = len(self.puzzle)//2
        print("len self.puzzle", len(self.puzzle))
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
                    print("having 3 in row")
                    return False
        #column
        for i in range(len(self.puzzle)):
            column = [row[i] for row in self.puzzle]
            for j in range(len(column)-2):
                if (column[j] == '0' and column[j+1] == '0' and column[j+2] == '0') or\
                        (column[j] == '1' and column[j+1] == '1' and column[j+2] == '1'):
                    print("having 3 in column")
                    return False


        return True

    def calculate_degree(self):
        print("calculate degree")
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


    def calling_methods(self):
        self.check_possible()
        self.calculate_degree()

puzzle_csp = Puzzle_csp()
puzzle_csp.calling_methods()
