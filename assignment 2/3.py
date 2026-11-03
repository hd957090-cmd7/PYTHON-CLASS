# Read input from user
num = int(input("Input: "))

print("Output:", end=" ")
# Find and print all numbers that divide 'num' perfectly
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()