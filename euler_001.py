def sum_of_multiples_n(n):
    sum = 0
    for number in range(n):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
            print(number, sum)
    print(sum)


sum_of_multiples_n(1000)
