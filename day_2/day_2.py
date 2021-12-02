def position(inputs: list[str]) -> int:
    depth = width = 0
    for input in inputs:
        dir, val = input.split()
        if dir == "forward":
            width += int(val)
        if dir == "down":
            depth += int(val)
        if dir == "up":
            depth -= int(val)

    return depth * width


def pos_aim(inputs: list[str]) -> int:
    aim = width = depth = 0
    for input in inputs:
        dir, val = input.split()
        if dir == "down":
            aim += int(val)
        if dir == "up":
            aim -= int(val)
        if dir == "forward":
            width += int(val)
            depth += int(val) * aim

    return width * depth


test_inputs = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
with open("day_2/inputs/inputs.txt") as f:
    lines = f.readlines()
    inputs = [line.strip() for line in lines]

print(pos_aim(inputs))
