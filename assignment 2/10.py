num=int(input("enter a number:"))
first=second=0
while num>0:
    digit=num%10
    if digit>first:
        second=first
        first=digit
    elif digit>second and digit!=first:
        second=digit
    num//=10
print("second largest digit:", second)