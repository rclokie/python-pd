import re


def partition(bottom, top, input):
    # print(f"top {top}, bottom {bottom}, input '{input}'")
    if (input == ""):
        return top
    elif re.match(r"[FL]", input[0]):
        return partition(bottom, int((top + bottom-1)/2), input[1:])
    elif re.match(r"[BR]", input[0]):
        return partition(int((bottom+top+1)/2), top, input[1:])
    else:
        raise Exception


def parseRow(input):
    return partition(0, 127, input[0:7])*8+partition(0, 7, input[7:10])


def main():
    with open("input.txt") as f:
        rows = list(map(lambda x: parseRow(x), f))
        maxval = max(rows)

        id = list(filter(lambda x: x not in rows and x +
                         1 in rows and x-1 in rows, range(0, maxval)))

    print(f"maxval is {maxval}")
    print(f"id is {id}")


if __name__ == "__main__":
    main()
