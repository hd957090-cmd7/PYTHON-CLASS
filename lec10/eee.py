# l=[10,20,30,40,50]

# def pl(l):
#     for i in range(len(l)):
#         print(l[i])

# pl(l)    

#Q>wrte a function to print all the digit of a given number {n=7369}

n=int(input())
print()
def dp(n):
    while(n!=0):
        id=n%10
        print(id)
        n=n//10
dp(n)

#Q>write a function to check a number is {1}palidrome{2}strong{3}arm strom{4}project

