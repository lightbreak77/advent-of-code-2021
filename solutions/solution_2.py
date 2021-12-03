from pathlib import Path

with (Path(__file__).parent / "../inputs/input-2.txt").open() as file:
    input_commands: list[str] = [line.rstrip() for line in file]

def part_1(commands: list[str]) -> int:
    horizontal_position: int = 0
    depth: int = 0

    command: str
    for command in commands:
        instruction: str = command.split()[0]
        value: int = int(command.split()[1])

        if instruction == "forward":
            horizontal_position += value
        elif instruction == "down":
            depth += value
        else:
            depth -= value

    return horizontal_position * depth

def part_2(commands: list[str]) -> int:
    horizontal_position: int = 0
    depth: int = 0
    aim: int = 0

    command: str
    for command in commands:
        instruction: str = command.split()[0]
        value: int = int(command.split()[1])

        if instruction == "forward":
            horizontal_position += value
            depth += aim * value
        elif instruction == "down":
            aim += value
        else:
            aim -= value

    return horizontal_position * depth

print(part_1(input_commands))

print(part_2(input_commands))