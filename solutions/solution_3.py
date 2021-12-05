from pathlib import Path

from typing import TextIO

def process(file: TextIO) -> list[str]:
    return [line.rstrip() for line in file]

def part_1(numbers: list[str]) -> int:
    gamma: str = ""
    epsilon: str = ""

    digit: int
    zeroes: int
    ones: int
    number: str
    for digit in range(len(numbers[0])):
        zeroes = 0
        ones = 0

        for number in numbers:
            if number[digit] == "0":
                zeroes += 1
            else:
                ones += 1

        if zeroes > ones:
            gamma += "0"
            epsilon += "1"
        elif ones > zeroes:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)

def part_2(numbers: list[str]) -> int:
    o2_numbers: list[str] = numbers

    co2_numbers: list[str] = numbers

    digit: int
    o2_zeroes: list[str]
    o2_ones: list[str]
    co2_zeroes: list[str]
    co2_ones: list[str]
    o2_number: str
    co2_number: str
    for digit in range(len(numbers[0])):
        o2_zeroes = []
        o2_ones = []

        co2_zeroes = []
        co2_ones = []

        if len(o2_numbers) > 1:
            for o2_number in o2_numbers:
                if o2_number[digit] == "0":
                    o2_zeroes.append(o2_number)
                else:
                    o2_ones.append(o2_number)

            if len(o2_ones) >= len(o2_zeroes):
                o2_numbers = o2_ones
            else:
                o2_numbers = o2_zeroes

        if len(co2_numbers) > 1:
            for co2_number in co2_numbers:
                if co2_number[digit] == "0":
                    co2_zeroes.append(co2_number)
                else:
                    co2_ones.append(co2_number)

            if len(co2_zeroes) <= len(co2_ones):
                co2_numbers = co2_zeroes
            else:
                co2_numbers = co2_ones

    return int(o2_numbers[0], 2) * int(co2_numbers[0], 2)

with (Path(__file__).parent / "../inputs/input-3.txt").open() as input_file:
    input_numbers: list[str] = process(input_file)

print(part_1(input_numbers))

print(part_2(input_numbers))