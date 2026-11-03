n = int(input("Enter the number of elements: "))

largest = float('-inf')
second_largest = float('-inf')

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print("Output:", second_largest)