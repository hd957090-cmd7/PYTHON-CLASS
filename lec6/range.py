#num = int(input())
#print()
#for i in range(1,11):
#    print(num)



#n=int(input())
#for i in range (n,0,-1):
#    print(i)



#Q  sum of first 5 natural no.   
#n=int (input())
#t=0
#for i in range(1,n+1):
#    t+=i
#    print(t)



# Q a given no. is prime no. or not
n=int(input())
count=0
for i in range(1,n+1):
        if(n%i==0):
            count+=1
#check for prime
#if (count==2):
#        print("is prime no.")
#else:
#       print("is not prime no.")
#or check for prime
if (count==2):
        print(f"given no. {n} is a prime no.")
else:
        print(f"given no. {n} is not a prime")