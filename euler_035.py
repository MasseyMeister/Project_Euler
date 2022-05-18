from time import time

def is_prime1(input):

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




def is_prime2(number):
    """returns True for a prime number, False otherwise."""
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            return False
        factor += 1
    return True

def circulate(number):
    """returns all circulations of a number."""
    for n in str(number):
        if not int(n) % 2:
            return False
    circulations = []
    digits = list(str(number))
    for i in range(len(str(number))):
        last = digits.pop()
        circulations.append(last + ''.join(digits))
        digits = [last] + digits
    return [int(x) for x in circulations]


def circular_primes(limit):
    """returns all circular primes below limit."""
    all_circulations = [2]
    for num in range(3, limit, 2):
        if is_prime2(num):
            check = 0
            if circulate(num):
                circulations = circulate(num)
                for circulation in circulations:
                    if not is_prime2(circulation):
                        check += 1
                if not check:
                    all_circulations.extend(circulations)
    return all_circulations


if __name__ == '__main__':
    start_time = time()
    print(len(set(circular_primes(200000))))
    print(f'Time: {time() - start_time} seconds.')