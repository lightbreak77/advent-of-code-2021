from pathlib import Path

from typing import TextIO

def process(file: TextIO) -> list[int]:
    return [int(lanternfish) for lanternfish in file.readline().split(",")]

def part_1(lanternfishes: list[int]) -> int:
    temp_lanternfishes: list[int] = lanternfishes.copy()
    temp_temp_lanternfishes: list[int]
    index: int
    for day in range(80):
        temp_temp_lanternfishes = temp_lanternfishes.copy()
        index = 0
        for lanternfish in temp_lanternfishes:
            if lanternfish == 0:
                temp_temp_lanternfishes.append(8)
                temp_temp_lanternfishes[index] = 6
            else:
                temp_temp_lanternfishes[index] -= 1
            index += 1

        temp_lanternfishes = temp_temp_lanternfishes

    return len(temp_lanternfishes)

def part_2(lanternfishes: list[int]) -> int:
    lanternfish_timers: list[int] = [0 for i in range(9)]

    lanternfish: int
    for lanternfish in lanternfishes:
        lanternfish_timers[lanternfish] += 1

    index: int
    for day in range(256):
        temp_lanternfish_timers = lanternfish_timers.copy()
        lanternfish_timers = [0 for i in range(9)]

        for index in range(9):
            if index == 0:
                lanternfish_timers[8] += temp_lanternfish_timers[0]
                lanternfish_timers[6] += temp_lanternfish_timers[0]
            else:
                lanternfish_timers[index - 1] += temp_lanternfish_timers[index]

    return sum(lanternfish_timers)

with (Path(__file__).parent / "../inputs/input-6.txt").open() as input_file:
    input_lanternfishes: list[int] = process(input_file)

print(part_1(input_lanternfishes))

print(part_2(input_lanternfishes))