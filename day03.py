# part 1

claims_for_square = {}

with open("./day03-input.txt") as claims:
    for claim in claims:
        claim_details = claim.split(" ")
        margins = claim_details[2][:-1].split(",")
        left_margin = int(margins[0])
        top_margin = int(margins[1])

        dimensions = claim_details[3].split("x")
        width = int(dimensions[0])
        height = int(dimensions[1])

        for column_number in range(top_margin + 1, top_margin + height + 1):
            for row_number in range(left_margin + 1, left_margin + width + 1):
                if (column_number, row_number) in claims_for_square.keys():
                    claims_for_square[(column_number, row_number)] += 1
                else:
                    claims_for_square[(column_number, row_number)] = 1

disputed = 0

for key, value in claims_for_square.items():
    if value > 1:
        disputed += 1

print(disputed)


# part 2

def find_intact_claim():
    with open("./day03-input.txt") as claims:
        for claim in claims:
            claim_details = claim.split(" ")
            margins = claim_details[2][:-1].split(",")
            left_margin = int(margins[0])
            top_margin = int(margins[1])

            dimensions = claim_details[3].split("x")
            width = int(dimensions[0])
            height = int(dimensions[1])

            claim_id = claim_details[0][1:]

            next_claim = False

            for column_number in range(top_margin + 1, top_margin + height + 1):
                if next_claim:
                    break
                for row_number in range(left_margin + 1, left_margin + width + 1):
                    if (claims_for_square[(column_number, row_number)]) > 1:
                        next_claim = True
                        break
            
            if not next_claim:
                print(claim_id)
                return

find_intact_claim()