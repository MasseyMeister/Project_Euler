numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

max = 100
counter = 0
for n in range(max):

    for i in numbers:
        a = (len(str(i**n)))
        if a == n:
            print(a, i**n)
            print(i, n)
            counter += 1

print(counter)
