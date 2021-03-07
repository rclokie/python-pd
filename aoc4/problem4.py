import re


class Passport:
    REQUIRED = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    OPTIONAL = ["cid"]

    def __init__(self, data):
        self.fields = {}
        for match in re.finditer(r"(\w+):(\S+)", data):
            self.fields[match.group(1)] = match.group(2)
        # self.printPassport()

    def printPassport(self):
        for k, v in self.fields.items():
            print(f"{k}:{v}", end=' ')
        print("valid") if self.validate1() else print("invalid")

    def validate1(self):
        if all(key in self.fields for key in self.REQUIRED):
            return True
        else:
            return False

    # def validate2(self):
    #     if not all(key in self.fields for key in self.REQUIRED):
    #         return False
    #     if not (len(self.fields["byr"]) == 4 and  1920 <= int(self.fields["byr"]) <= 2002):
    #         return False
    #     if not (len(self.fields["iyr"])== 4 and  2010 <= int(self.fields["iyr"]) <= 2020):
    #         return False
    #     if not (len(self.fields["eyr"]) == 4 and  2020 <= int(self.fields["eyr"]) <= 2030):
    #         return False


    #     # i cant be bothered making these look consistent
    #     if not validateHgt(): return False
    #     if not validateHcl(): return False
    #     if not validateEcl(): return False
    #     if not validatePid(): return False
    #     if not validateCid(): return False

    #     return True

        

    # def validateHgt(self):
    #     match = re.search(r"(\d{2,3})(\w\w)",self.fields["hgt"])

    #     if match == None: return False
    #     if (match.group(2) == "cm" and 150 <= int(match.group(1)) <= 193 ): 
    #         None
    #     elif (match.group(2) == "in" and 59 <= int(match.group(1)) <= 76 ):
    #         None
    #     else:
    #         print(f"invalid height")
    #         return False
    #     return True

    # def validateHcl(self):
    #     return True

    # def validateEcl(self):
    #     return True

    # def validatePid(self):
    #     return True

    # def validateCid(self):
    #     return True


def main():
    passports = []
    with open("input.txt") as f:
        for passportLine in f.read().split("\n\n"):
            passports.append(Passport(passportLine.replace("\n"," ")))

    count = len([p for p in passports if p.validate2()])
    print(f"count is {count}, num passports is {len(passports)}")


if __name__ == "__main__":
    main()
