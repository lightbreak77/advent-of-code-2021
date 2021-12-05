from pathlib import Path

from typing import TextIO

def process(file: TextIO) -> list[int]:
    return [int(line) for line in file]

def part_1(measurements: list[int]) -> int:
    answer: int = 0

    index: int
    for index in range(len(measurements) - 1):
        if measurements[index + 1] > measurements[index]:
            answer += 1
    
    return answer

def part_2(measurements: list[int]) -> int:
    answer: int = 0

    index: int
    for index in range(len(measurements) - 3):
        if sum(measurements[index + 1 : index + 4]) > sum(measurements[index : index + 3]):
            answer += 1

    return answer

with (Path(__file__).parent / "../inputs/input-1.txt").open() as input_file:
    input_measurements: list[int] = process(input_file)

print(part_1(input_measurements))

print(part_2(input_measurements))