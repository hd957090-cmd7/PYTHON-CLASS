number = int(input("Input: "))

# Handle the special case where the input number is 0
if number == 0:
    print("Output: 0:1")
else:
    # Check each possible digit from 0 to 9
    for digit in range(10):
        frequency = 0
        temp = number
        
        # Count how many times the current digit appears
        while temp > 0:
            current_digit = temp % 10
            if current_digit == digit:
                frequency += 1
            temp //= 10
            
        # Only print the frequency if the digit was present
        if frequency > 0:
            print(f"{digit}:{frequency}", end=", ")
    print()