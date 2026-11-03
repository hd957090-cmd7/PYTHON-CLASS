#Q>count all the number from 1 to n which are divisible by 5 And 3.
#i=1
#n=int(input("enter the number:"))
#while (i<=n):
#    if(i%3==0 and i%5==0):
#        print(i)
#    i+=1





#Q>check if the number is perfect number or not
number = int(input("Input: "))

factor_sum = 0
for i in range(1, number):
    if number % i == 0:
        factor_sum += i

if factor_sum == number:
    print("Output: Perfect Number")
else:
    print("Output: Not a Perfect Number")