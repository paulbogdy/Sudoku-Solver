import random


class SudokuTable:
    """
    A class used to represent a sudoku table
    """

    def __init__(self):
        self.__table = [[0 for _ in range(9)] for _ in range(9)]
        self.__possible_values = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for _ in range(9)]

    def __setitem__(self, key, value):
        x, y = key
        if value != 0 and value not in self.__possible_values[x][y]:
            raise ValueError("Wrong value!")
        initial_value = self.__table[x][y]
        self.__table[x][y] = value
        if not self.check_validity():
            self.__table[x][y] = initial_value
            raise ValueError("Wrong value!")
        else:
            self.update_memory()

    def __getitem__(self, item):
        x, y = item
        return self.__table[x][y]

    def update_memory(self):
        for x in range(9):
            for y in range(9):
                self.__possible_values[x][y] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(9):
                    if self.__table[i][y] in self.__possible_values[x][y]:
                        self.__possible_values[x][y].remove(self.__table[i][y])
                for j in range(9):
                    if self.__table[x][j] in self.__possible_values[x][y]:
                        self.__possible_values[x][y].remove(self.__table[x][j])
                for i in range(int(x / 3) * 3, int(x / 3) * 3 + 3):
                    for j in range(int(y / 3) * 3, int(y / 3) * 3 + 3):
                        if self.__table[i][j] in self.__possible_values[x][y]:
                            self.__possible_values[x][y].remove(self.__table[i][j])

    def check_validity(self):
        for x in range(9):
            elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for y in range(9):
                if self.__table[x][y] != 0:
                    try:
                        elements.remove(self.__table[x][y])
                    except:
                        return False
        for y in range(9):
            elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for x in range(9):
                if self.__table[x][y] != 0:
                    try:
                        elements.remove(self.__table[x][y])
                    except:
                        return False
        for x in range(3):
            for y in range(3):
                elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for i in range(x * 3, x * 3 + 3):
                    for j in range(y * 3, y * 3 + 3):
                        if self.__table[i][j] != 0:
                            try:
                                elements.remove(self.__table[i][j])
                            except:
                                return False
        return True

    def set_uniques(self):
        ok = True
        while ok:
            ok = False
            for x in range(9):
                for y in range(9):
                    if len(self.__possible_values[x][y]) == 1:
                        self.__setitem__((x, y), self.__possible_values[x][y][0])
                    ok = True

    def is_solved(self):
        for x in range(9):
            for y in range(9):
                if self.__possible_values[x][y]:
                    return False
        return True

    def solve(self):
        if self.is_solved():
            return True
        len_min = 10
        x = 0
        y = 0
        for i in range(9):
            for j in range(9):
                if self.__table[i][j] == 0 and len(self.__possible_values[i][j]) < len_min:
                    x = i
                    y = j
                    len_min = len(self.__possible_values[i][j])
        for k in range(len_min):
            self.__setitem__((x, y), self.__possible_values[x][y][k])
            if self.solve():
                return True
            self.__setitem__((x, y), 0)
        return False

    def clear(self):
        self.__table = [[0 for _ in range(9)] for _ in range(9)]
        self.__possible_values = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for _ in range(9)]

    def generate(self, number):
        for _ in range(10):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if self.__possible_values[x][y]:
                self.__setitem__((x, y), random.choice(self.__possible_values[x][y]))
        self.solve()
        blocks = []
        for i in range(9):
            for j in range(9):
                blocks.append((i, j))
        for _ in range(number):
            x, y = random.choice(blocks)
            self.__setitem__((x, y), 0)
            blocks.remove((x, y))
