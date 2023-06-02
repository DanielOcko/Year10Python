import time

def isPrime(number):
    for d in range(2, number):
        if number%d == 0:
            return False
    return True

maxNum = 10000
primes = []

start_time = time.perf_counter()
for i in range(2, maxNum):
    if isPrime(i):
        primes.append(i)
end_time = time.perf_counter()
print(primes)

print(f"finished in {end_time - start_time} seconds!")
