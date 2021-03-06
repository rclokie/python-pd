import re


class Passport:
    REQUIRED = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    OPTIONAL = ["cid"]

    def __init__(self, data):
        self.fields = {}
        for match in re.finditer(r"(\w+):(\S+)", data):
            self.fields[match.group(1)] = match.group(2)
        self.printPassport()

    def printPassport(self):
        for k, v in self.fields.items():
            print(f"{k}:{v}", end=' ')
        print("valid") if self.validate1() else print("invalid")

    def validate1(self):
        if all(key in self.fields for key in self.REQUIRED):
            return True
        else:
            return False


def main():
    passports = []
    block = ""
    with open("input.txt") as f:
        for line in f:
            if line == "\n":
                if (block != ""):
                    passports.append(Passport(block))
                block = ""
            else:
                block = block + " " + line.strip("\n")

    count = len([p for p in passports if p.validate1()])
    print(f"count is {count}, num passports is {len(passports)}")
# TODO dropping at least one input line


if __name__ == "__main__":
    main()
