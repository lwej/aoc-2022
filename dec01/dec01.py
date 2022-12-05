import functools


def add_list_entries(total, elf_cals):
    return total + elf_cals


total_cals = []
elf = []

# Open file and parse
with open("input", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line != "\n":
            elf.append(int(line))
            total = functools.reduce(add_list_entries, elf)

        if line == "\n":
            total_cals.append(total)
            elf.clear()

sorted_list = sorted(total_cals, reverse=True)
total_top_three = sorted_list[0] + sorted_list[1] + sorted_list[2]

print(f"Answer 1: {max(total_cals)}\n" f"Answer 2: {total_top_three}")
