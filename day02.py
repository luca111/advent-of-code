# part 1

twice = 0
thrice = 0

with open("./day02-input.txt") as ids:
    for id in ids:
        letters_frequency = {}
        for letter in id:
            if letter in letters_frequency.keys():
                letters_frequency[letter] += 1
            else:
                letters_frequency[letter] = 1
        if 2 in letters_frequency.values():
            twice += 1
        if 3 in letters_frequency.values():
            thrice += 1

print(twice * thrice)

# part 2


def get_similar_ids():
    with open("./day02-input.txt") as ids:
        past_ids = []
        for id in ids:
            length = len(id)
            for past_id in past_ids:
                same_letters = []
                for index, value in enumerate(id):
                    if value == past_id[index]:
                        same_letters.append(value)
                if len(same_letters) == length - 1:
                    print("".join(same_letters))
                    return
            past_ids.append(id)


get_similar_ids()
