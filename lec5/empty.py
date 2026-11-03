#i = 1
#
#while (i<=10):
#    print(i)
#    i+=1            #infinite loop incase i+=1 is not present


#Q take input from user for a correct number until he guess it correctly.
h = 10
n=int(input("guess the no.:"))

while(h !=n):
    n = int(input("enter your guess:"))
print(f"{n}is the correct guess!!")