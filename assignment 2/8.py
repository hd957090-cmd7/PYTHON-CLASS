num = int(input("Input: "))

# Count the number of digits mathematically
temp = num
num_digits = 0
while temp > 0:
    num_digits += 1
    temp //= 10

# Calculate the sum of digits raised to the power of total digits
temp = num
armstrong_sum = 0
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10

if armstrong_sum == num:
    print("Output: Armstrong Number")
else:
    print("Output: Not an Armstrong Number")