import re

with open("input", "r") as f:
    input_data = f.readlines()

COUNT = 0
OVERLAP = 0


def count_contains(lines: list):
    global COUNT
    for line in lines:
        # regex only digits
        find_digits = (re.findall(r"\d*[^-,\n]\d*", line))
        digits = [int(x) for x in find_digits]
        assignment1 = [*range(digits[0], (digits[1] + 1), 1)]
        assignment2 = [*range(digits[2], (digits[3] + 1), 1)]
        if set(assignment2).issubset(set(assignment1)) or set(
                assignment1).issubset(set(assignment2)):
            COUNT += 1


def count_overlap(lines):
    global OVERLAP
    for line in lines:
        # regex only digits
        find_digits = (re.findall(r"\d*[^-,\n]\d*", line))
        digits = [int(x) for x in find_digits]
        x = range(digits[0], (digits[1] + 1))
        y = range(digits[2], (digits[3] + 1))

        if max(x.start, y.start) < min(x.stop, y.stop):
            OVERLAP += 1


count_overlap(input_data)
count_contains(input_data)
print(f"Contains eachother: {COUNT}\nOverlaps: {OVERLAP}")
