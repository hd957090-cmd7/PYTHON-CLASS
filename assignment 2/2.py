# Read input from user
n = int(input("Input: "))

prime_sum = 0

# Loop through numbers from 2 up to n
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num

print("Output:", prime_sum)