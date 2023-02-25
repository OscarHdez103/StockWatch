def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    if n <= 0:
        return None
    prime_counter = 0
    num = 2
    while prime_counter < n:
        if is_prime(num):
            prime_counter += 1
        num += 1
    return num - 1

print(nth_prime(10))