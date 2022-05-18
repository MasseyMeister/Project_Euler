def check_prime(input):

    if input == 2:
        return 1
    if input % 2 == 0:
        return 0

    for x in range(input):
        if x == 0:
            continue
        if x == 1:
            continue
        if input % x == 0:
            break
        if x == input - 1:
            return 1
    return 0


def find_n_prime(n):

    counter = 1
    prime_counter = 1
    while prime_counter < n + 1:

        if check_prime(counter):
            print(prime_counter, counter)
            prime_counter += 1

        counter += 1
    print(counter)


check_prime(4)
