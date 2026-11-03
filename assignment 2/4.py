number = int(input("Input: "))

factor_sum = 0
for i in range(1, number):
    if number % i == 0:
        factor_sum += i

if factor_sum == number:
    print("Output: Perfect Number")
else:
    print("Output: Not a Perfect Number")