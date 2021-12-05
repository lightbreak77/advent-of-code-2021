from pathlib import Path

from typing import TextIO

def process(file: TextIO) -> list[list[list[int]]]:
    lines: list[list[list[int]]] = []

    lines_str: list[list[str]] = [line.split("->") for line in file]

    for coordinates in lines_str:
        line_start = [int(coordinates[0].split(",")[0]), int(coordinates[0].split(",")[1])]
        line_end = [int(coordinates[1].split(",")[0]), int(coordinates[1].split(",")[1])]

        lines.append([line_start, line_end])

    return lines

def part_1(lines: list[list[list[int]]]):
    answer: int = 0

    dangers: dict[str: int] = {}

    line: list[list[int]]
    line_dangers: list[str]
    x: int
    y: int
    danger: str
    for line in lines:
        line_dangers = []

        if line[0][0] == line[1][0]:
            if line[0][1] == line[1][1]:
                line_dangers.append(str(line[0][0]) + ", " + str(line[0][1]))
            elif line[0][1] < line[1][1]:
                for y in range(line[0][1], line[1][1] + 1):
                    line_dangers.append(str(line[0][0]) + ", " + str(y))
            else:
                for y in range(line[1][1], line[0][1] + 1):
                    line_dangers.append(str(line[0][0]) + ", " + str(y))

        elif line[0][1] == line[1][1]:
            if line[0][0] < line[1][0]:
                for x in range(line[0][0], line[1][0] + 1):
                    line_dangers.append(str(x) + ", " + str(line[0][1]))
            else:
                for x in range(line[1][0], line[0][0] + 1):
                    line_dangers.append(str(x) + ", " + str(line[0][1]))

        for danger in line_dangers:
            if danger in dangers:
                dangers[danger] += 1
            else:
                dangers[danger] = 1

    danger_value: int
    for danger_value in dangers.values():
        if danger_value >= 2:
            answer += 1
    
    return answer

def part_2(lines: list[list[list[int]]]):
    answer: int = 0

    dangers: dict[str: int] = {}

    line: list[list[int]]
    line_dangers: list[str]
    x: int
    y: int
    danger: str
    for line in lines:
        line_dangers = []

        if line[0][0] == line[1][0]:
            if line[0][1] == line[1][1]:
                line_dangers.append(str(line[0][0]) + ", " + str(line[0][1]))
            elif line[0][1] < line[1][1]:
                for y in range(line[0][1], line[1][1] + 1):
                    line_dangers.append(str(line[0][0]) + ", " + str(y))
            else:
                for y in range(line[1][1], line[0][1] + 1):
                    line_dangers.append(str(line[0][0]) + ", " + str(y))

        elif line[0][1] == line[1][1]:
            if line[0][0] < line[1][0]:
                for x in range(line[0][0], line[1][0] + 1):
                    line_dangers.append(str(x) + ", " + str(line[0][1]))
            else:
                for x in range(line[1][0], line[0][0] + 1):
                    line_dangers.append(str(x) + ", " + str(line[0][1]))

        elif line[0][0] < line[1][0] and line[0][1] < line[1][1]:
            temp_coordinate: list[int] = line[0]

            while temp_coordinate != line[1]:
                line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))

                temp_coordinate[0] += 1
                temp_coordinate[1] += 1

            line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))

        elif line[0][0] < line[1][0] and line[0][1] > line[1][1]:
            temp_coordinate: list[int] = line[0]

            while temp_coordinate != line[1]:
                line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))

                temp_coordinate[0] += 1
                temp_coordinate[1] -= 1

            line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))

        elif line[0][0] > line[1][0] and line[0][1] > line[1][1]:
            temp_coordinate: list[int] = line[0]

            while temp_coordinate != line[1]:
                line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))

                temp_coordinate[0] -= 1
                temp_coordinate[1] -= 1

            line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))   

        else:
            temp_coordinate: list[int] = line[0]

            while temp_coordinate != line[1]:
                line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))

                temp_coordinate[0] -= 1
                temp_coordinate[1] += 1

            line_dangers.append(str(temp_coordinate[0]) + ", " + str(temp_coordinate[1]))  

        for danger in line_dangers:
            if danger in dangers:
                dangers[danger] += 1
            else:
                dangers[danger] = 1   

    danger_value: int
    for danger_value in dangers.values():
        if danger_value >= 2:
            answer += 1
    
    return answer

with (Path(__file__).parent / "../inputs/input-5.txt").open() as input_file:
    input_lines: list[list[list[int]]] = process(input_file)

print(part_1(input_lines))

print(part_2(input_lines))