from src.SudokuTable import SudokuTable
from src.UI import GUI


if __name__ == '__main__':
    table = SudokuTable()
    gui = GUI(table)
    gui.run()
