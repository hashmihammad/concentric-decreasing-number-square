x = int(input())
print("\n\n\n\n")

for i in range(2 * x - 1):
    if i < x:
        row = i
    else:
        row = 2 * x - 2 - i

    for j in range(row):
        print(x - j, end="  ")

    middle_value = x - row
    for _ in range(2 * (x - row) - 1):
        print(middle_value, end="  ")

    for j in range(row):
        print(middle_value + j + 1, end="  ")

    print("")
