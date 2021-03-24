from functools import reduce


def part1():
    answers = []
    with open("input.txt") as f:
        answers = list(
            map(lambda x: set(x.replace("\n", "")), f.read().split("\n\n")))

    print(f"answers is {answers}")
    sum = reduce(lambda a, b: a+len(b), answers, 0)

    print(f"sum is {sum}")


def parseGroup(group):
    members = list(map(set, group.split("\n")))
    # print(f"members is {members}")
    answers = reduce(lambda x, y: x.intersection(y), members)
    # print(f"answers is {answers}, len answers is {len(answers)}")
    return len(answers)


def part2():
    with open("input.txt") as f:
        sum = reduce(lambda a, b: a+parseGroup(b), f.read().split("\n\n"), 0)
        # note that i cheated here and put an extra newline on the end of my input file
        # because i couldnt be bothered working out how to strip the empty line from
        # the last one :(
    print(f"sum is {sum}")


def part2_oneliner():
    # for entertainment purposes only
    sum = reduce(lambda a, b: a + len(reduce(lambda x, y: x.intersection(y),
                                             list(map(set, b.split("\n"))))), open("input.txt").read().split("\n\n"), 0)
    print(f"sum is {sum}")


def main():
    # part1()
    # part2()
    part2_oneliner()


if __name__ == "__main__":
    main()
