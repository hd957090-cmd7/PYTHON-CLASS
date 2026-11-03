x={1,2,3,4,5,1,2,3,4,5}
y={6,7,8,9,10}
print(x)
em_dict = {}
emp_set = set()

print("empty set" ,emp_set)

print(x-y)#common word/variable are remove
print(x|y)#union

y.discard(6)#remove 6 from y
print(y)

print(x.issubset(y))#check if x is subset of y or not
z=[1,2,3,4,5]
print(z.append(6))#add 6 to z
print(z)

r={"stu":"John","section":"A","marks":85}
r.pop("marks")#remove marks from r
print(r)

r.popitem()#remove last item from r
print(r)

r.clear()#clear all items from r
print(r)

