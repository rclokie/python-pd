class Passport:

    def __init__(self, data):

        print(f"data is {data}")


def main():
    passports = []
    block = ""
    with open("input_short.txt") as f:
        for line in f:
            if line == "\n":
                passports.append(Passport(block))
                block = ""
            else:
                block = block + " " + line.strip("\n")


if __name__ == "__main__":
    main()
