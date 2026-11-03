#write function to swap 1st and last element of a given number t=(10,20,30,40) expected output=(10,)
# t=(10,)
# def swap(t):
#     if len(t)<2:
#         return t
#     result=(t[-1],)+t[1:-1]+(t[0],)
#     return result
# print(swap(t))

#Q>write a funtion to rotate a given tuple by k position  t=(10,20,30,40,50) k=2 expected output=(50,10,20,30,40)
t=(10,20,30,40,50)
def rotate(t,k):
    k = k%len(t)
    return t[-2:]+t[:-2]
print(rotate(t,2))