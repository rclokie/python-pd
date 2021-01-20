
# part 1 - find the number of valid passwords
# part 2 -

class Password:
    min_reps = 0
    max_reps = 0
    letter = ''
    text = ''

    def validate(self):
        count = self.text.count(self.letter)
        retval = self.min_reps <= count <= self.max_reps
        print(
            f"{self.text} has {count} occurrences of {self.letter}, returning {retval}")
        return retval

    def validate_pt2(self):
        present1 = False
        present2 = False
        try:
            present1 = self.text[self.min_reps-1] == self.letter
        except Exception as identifier:
            pass
        try:
            present2 = self.text[self.max_reps-1] == self.letter
        except Exception as identifier:
            pass

        retval = present1 ^ present2
        print(
            f"{self.min_reps}, {self.max_reps}, {self.letter}, {self.text}, {present1}, {present2} validates as {retval}")
        return retval

    def __init__(self, line):
        (minmax, self.letter, self.text) = line.split()
        self.letter = self.letter[0]
        (minstr, maxstr) = minmax.split('-')
        self.min_reps = int(minstr)
        self.max_reps = int(maxstr)


passwords = []

with open("input.txt") as f:
    for line in f:
        try:
            passwords.append(Password(line))
        except Exception as e:
            print(f"{e}")

count = 0
for password in passwords:
    if password.validate_pt2():
        count += 1

print(f"count is {count}")
