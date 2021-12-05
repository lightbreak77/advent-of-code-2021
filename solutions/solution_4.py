from pathlib import Path

from typing import TextIO

def process(file: TextIO) -> tuple[list[str], list[list[list[str]]]]:
    numbers: list[str] = [number.rstrip() for number in file.readline().split(",")]

    boards: list[list[list[str]]] = []

    line: str
    board: list[list[str]]
    for line in file:
        if line == "\n":
            board = []
        else:
            board.append([board_number.rstrip() for board_number in line.split()])
        
        if len(board) == 5:
            boards.append(board)

    return numbers, boards

def part_1(data: tuple[list[str], list[list[list[str]]]]):
    numbers: list[str] = data[0]
    boards: list[list[list[str]]] = data[1]

    score: int = 0

    temp_boards: list[list[list[str]]] = boards
    temp_temp_boards: list[list[list[str]]] = boards
    number: str
    board: list[list[str]]
    row: list[str]
    board_number: str
    column_index: int
    column: list[str]
    is_win: bool = False
    for number in numbers:
        for board in temp_boards:
            for row in board:
                for board_number in row:
                    if board_number == number:
                        temp_temp_boards[temp_boards.index(board)][board.index(row)][row.index(board_number)] = "marked"

        temp_boards = temp_temp_boards

        for board in temp_boards:
            for row in board:
                if all([number_status == "marked" for number_status in row]):
                    is_win = True

            for column_index in range(5):
                column = []

                for row in board:
                    column.append(row[column_index])
                
                if all([number_status == "marked" for number_status in column]):
                    is_win = True   

            if is_win:
                for row in board:
                    for board_number in row:
                        if board_number != "marked":
                            score += int(board_number)

                return score * int(number)

def part_2(data: tuple[list[str], list[list[list[str]]]]):
    numbers: list[str] = data[0]
    boards: list[list[list[str]]] = data[1]


    score: int = 0

    temp_boards: list[list[list[str]]] = boards
    temp_temp_boards: list[list[list[str]]] = boards
    number: str
    board: list[list[str]]
    row: list[str]
    board_number: str
    column_index: int
    column: list[str]
    is_win: bool
    for number in numbers:
        for board in temp_boards:
            for row in board:
                for board_number in row:
                    if board_number == number:
                        temp_temp_boards[temp_boards.index(board)][board.index(row)][row.index(board_number)] = "marked"

        temp_boards = temp_temp_boards

        for board in temp_boards:
            is_win = False

            for row in board:
                if all([number_status == "marked" for number_status in row]):
                    is_win = True

            for column_index in range(5):
                column = []

                for row in board:
                    column.append(row[column_index])
                
                if all([number_status == "marked" for number_status in column]):
                    is_win = True   

            if is_win:
                if len(temp_temp_boards) > 1:
                    temp_temp_boards.remove(board)
                else:
                    for row in board:
                        for board_number in row:
                            if board_number != "marked":
                                score += int(board_number)
                    return score * int(number)

        temp_boards = temp_temp_boards


with (Path(__file__).parent / "../inputs/input-4.txt").open() as input_file:
    input_data: tuple[list[str], list[list[list[str]]]] = process(input_file)

print(part_1(input_data))

print(part_2(input_data))