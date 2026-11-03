num = int(input("Input: "))

# Find the total number of digits to determine the place value position
temp = num
multiplier = 1
while temp >= 10:
    temp //= 10
    multiplier *= 10

last_digit = num % 10
remaining_digits = num // 10

# Move the last digit to the front
shifted_num = (last_digit * multiplier) + remaining_digits

print("Output:", shifted_num)