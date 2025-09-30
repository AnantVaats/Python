def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(start,end):
    prime_nums = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_nums.append(num)
    return prime_nums

print(prime_numbers_in_range(10, 30))
