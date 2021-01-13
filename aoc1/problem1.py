
# part 1 - find two numbers that sum to 2020, print their product
# part 2 - find three numbers that sum to 2020, print their product
input_data = []
input_ints = []
with open("input.txt") as f:
    for line in f:
        try:
            input_ints.append(int(line))
        except expression as identifier:
            pass

for first in input_ints:
    for second in input_ints:
        for third in input_ints:
            if first + second + third == 2020:
                print(f"{first} + {second} + {third} = {first+second+third}")
                print(f"{first * second * third}")
