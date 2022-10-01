from typing import List

NCOLS = 9
NROWS = 9


class Element:
    def __init__(
            self, 
            value: int, 
            row: int, 
            col: int
        ):
        self.value = value
        self.row = row
        self.col = col
        self.potentials = []

    def is_solved(self):
        return bool(self.value)
    
    def __repr__(self) -> str:
        return f"({self.row},{self.col}): {self.value}"
    
    def update(self, potentials: List[int]) -> bool:
        self.potentials = potentials
        if len(self.potentials) == 1:
            self.value = list(self.potentials)[0]
            print(self)
            return True
        return False

Sudoku = List[List[Element]]


def read_sudoku(file_path: str):
    with open(file_path) as f:
        return [
            [
                Element(int(value.strip()), row, col)
                for col, value in enumerate(
                    line.split(",")
                )
            ]
            for row, line in enumerate(f.readlines())
        ]
        

def solve_element(
        sudoku: Sudoku, 
        row: int, 
        col: int
    ) -> List[int]:
    potentials = set(range(1, 10))
    for i in range(NROWS):
        for j in range(NCOLS):
            c = sudoku[i][j]
            
            if i == row and j == col:
                continue

            if i == row:
                potentials = rm(potentials, c.value)

            if j == col:
                potentials = rm(potentials, c.value)

            if int(i / 3) == int(row / 3) and int(j / 3) == int(col / 3):
                potentials = rm(potentials, c.value)

    return potentials


def solve_iter(sudoku: Sudoku) -> bool:
    updated = False
    for i in range(NROWS):
        for j in range(NCOLS):
            cell = sudoku[i][j]
            if cell.is_solved():
                continue
            potentials = solve_element(sudoku, i, j)
            updated = updated or cell.update(potentials)
    return updated

def rm(s: set, v: int) -> set:
    return s.difference({v})


if __name__ == "__main__":
    s = read_sudoku(
        "listener_april_3_9_2021_hard.csv"
    )
    while solve_iter(s):
        pass
