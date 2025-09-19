def is_prime_2(n):
    for i in range(2, n // 2):
        if n % i == 0:
            print(i)
            return False
    return True

def is_prime_3(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


from time import time

start = time()
is_prime_3(1000000021)
print(time() - start)