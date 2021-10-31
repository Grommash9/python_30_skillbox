import math

prime_numbers = [x for x in range(4, 1000) if all(x % y != 0 for y in range(2, int(math.sqrt(x)) + 1))]

print(prime_numbers)


all_numbers = [x for x in range(4, 1000)]
prime_numbers.clear()
for number in all_numbers:
    is_prime = True
    for divider in range(2, int(math.sqrt(number)) + 1):
        if number % divider == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)

print(prime_numbers)

