# part 1

frequencies_sum = 0

with open("./day01-input.txt") as frequencies_numbers:
    for number in frequencies_numbers:
        frequencies_sum += int(number)

print(frequencies_sum)


# part 2

solved = False
seen_frequencies = [0]
changes = []

with open("./day01-input.txt") as frequencies_numbers:
    for number in frequencies_numbers:
        new_frequency = seen_frequencies[-1] + int(number)
        if new_frequency in seen_frequencies:
            print(new_frequency)
            solved = True
            break
        else:
            seen_frequencies.append(new_frequency)
            changes.append(int(number))

while not solved:
    for number in changes:
        new_frequency = seen_frequencies[-1] + int(number)
        if new_frequency in seen_frequencies:
            print(new_frequency)
            solved = True
            break
        else:
            seen_frequencies.append(new_frequency)
            changes.append(number)
