import string
import fetch_input
priorities = []


def prioritize_all(line):
    compartment1 = line[: len(line) // 2]
    compartment2 = line[len(line) // 2:]
    for char in compartment1:
        if char in compartment2:
            priority = string.ascii_letters.index(char) + 1
            priorities.append(priority)
            return


def find_common_item(elf1, elf2, elf3):
    for letter in elf1:
        if letter in elf2 and letter in elf3:
            priority = string.ascii_letters.index(letter) + 1
            priorities.append(priority)
            return


with open("input", "r") as f:
    lines = f.readlines()
    #    for line in lines:
    #        sort_and_prioritize(line)
    it = iter(lines)
    for elf in it:
        elf1 = elf
        elf2 = next(it)
        elf3 = next(it)
        find_common_item(elf1, elf2, elf3)

print(f"Priorities: {sum(priorities)}\n")
