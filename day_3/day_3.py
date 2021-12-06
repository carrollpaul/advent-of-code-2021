from numpy import power
from collections import Counter


def power_consumption(report: list[str]) -> int:
    gamma = ""
    epsilon = ""
    for i in range(len(report[0])):
        cnt = Counter([x[i] for x in report])
        if cnt["0"] > cnt["1"]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def life_support(report: list[int]) -> int:
    oxy_report = report.copy()
    oxy_rating = ""
    while True:
        if len(oxy_report) == 1:
            oxy_rating = oxy_report[0]
            print(oxy_rating)
            return
        for i in range(len(report[0])):
            cnt = Counter([x[i] for x in oxy_report])
            if cnt["0"] > cnt["1"]:
                crit = "0"
            else:
                crit = "1"
            oxy_report = [x for x in oxy_report if x.startswith(crit)]
            print(oxy_report)


with open("day_3/inputs/report.txt") as f:
    report = [line.strip() for line in f.readlines()]

print(life_support(report))
