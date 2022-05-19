def divisible_by_all(limit):
    for i in range(60, 100000000000, 60):
        print(i)
        for j in range(1, limit + 1):
            if j == limit:
                return i
            if i % j == 0:
                continue
            else:
                break


print(divisible_by_all(20))
