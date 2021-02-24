
def main():
    geography = []

    with open("input.txt") as f:
        for line in f:
            try:
                geography.append(line.strip("\n"))
            except Exception as e:
                print(f"{e}")

    c1 = count_trees(geography, 1, 1)
    c2 = count_trees(geography, 3, 1)
    c3 = count_trees(geography, 5, 1)
    c4 = count_trees(geography, 7, 1)
    c5 = count_trees(geography, 1, 2)

    print(f"c1{c1},c2{c2},c3{c3},c4{c4},c5{c5}")
    print(f"product{c1*c2*c3*c4*c5}")


def count_trees(geography, deltax, deltay):
    x = 0
    y = 0
    count = 0

    while True:

        if geography[y][x] == "#":
            count += 1

        x = (x + deltax) % len(geography[y])
        y += deltay

        if y >= len(geography):
            break

    return count


if __name__ == "__main__":
    main()
