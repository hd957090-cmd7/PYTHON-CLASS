#typecasting
#float-integer
num = 45.5
print(type(num))
print(type(int(num)))
#int-string
print(type(str(num)))
#string-int
str ='888'
convert = int(str)
print(type(convert))
print(convert)
#(string-int) in this float form there are two process 
str2 = '4.98'
convert1 = float(str2)
convert2 = int(convert1)
print(convert2)
