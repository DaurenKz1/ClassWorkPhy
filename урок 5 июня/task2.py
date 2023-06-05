def is_prime(num, other = 2):
    if num <= 1:
        return False
    if other == num:
        return True
    if num % other == 0:
        return False
    else:
        return is_prime(num, other + 1)

print(is_prime(1))