def while_loop(m, n):
    i = 0
    numbers = []
    while i < m:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + n
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop(6, 1)