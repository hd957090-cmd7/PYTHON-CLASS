#Q> count no. of each vowel in a given string.
str = "vijay gold "
a=0
e=0
i=0
o=0
u=0
#membership operater  = in ,not in 
for i in str:
    if("a"==i or "A"==i):
        a+=1
    elif("e"==i or "E"==i):
        e+=1
    elif("i"==i or "I"==i):
        i+=1
    elif("o"==i or "O"==i):
        o+=1
    elif("u"==i or "U"==i):
        u+=1
print("count of a:",a)
print("count of e:",e)
print("count of i:",i)
print("count of o:",o)
print("count of u:",u)
