from tabnanny import check


def check_prime(number):
    """returns True for a prime number, False otherwise."""
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            return False
        factor += 1
    return True


number = 600851475143

list_of_primes = []
prime_factors = []

for i in range(2, 1000000):
    if check_prime(i):
        list_of_primes.append(i)

for prime in list_of_primes:
    if number % prime == 0:
        number = number/prime
        print(number)
        prime_factors.append(prime)
        continue
    else:
        continue

print(prime_factors)
