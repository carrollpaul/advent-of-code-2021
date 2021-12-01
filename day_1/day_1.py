def depth(depths: list[int]) -> int:
    cnt = 0
    for i in range(1, len(depths)):
        if depths[i - 1] < depths[i]:
            cnt += 1
    return cnt


def depth_windows(depths: list[int], k: int = 3) -> int:
    frames = [sum(depths[i : i + k]) for i in range(len(depths) - k + 1)]
    return depth(frames)


if __name__ == "__main__":
    with open("day_1/inputs/depths.txt") as f:
        depths = [int(line.strip()) for line in f.readlines()]

    print(depth_windows(depths))
