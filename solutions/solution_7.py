from pathlib import Path

from typing import TextIO

def process(file: TextIO) -> list[int]:
    return [int(crab) for crab in file.readline().split(",")]

def part_1(crabs: list[int]) -> int:
    furthest_position: int = max(crabs)

    fuel: list[int] = [0 for i in range(furthest_position + 1)]

    crab: int
    for position in range(furthest_position + 1):
        for crab in crabs:
            fuel[position] += abs(crab - position)

    return min(fuel)

def part_2(crabs: list[int]) -> int:
    furthest_position: int = max(crabs)

    fuel: list[float] = [0 for i in range(furthest_position + 1)]

    crab: int
    difference: int
    for position in range(furthest_position + 1):
        for crab in crabs:
            difference = abs(crab - position)
            fuel[position] += difference * (difference + 1) * 0.5

    return int(min(fuel))

with (Path(__file__).parent / "../inputs/input-7.txt").open() as input_file:
    input_crabs: list[int] = process(input_file)

print(part_1(input_crabs))

print(part_2(input_crabs))