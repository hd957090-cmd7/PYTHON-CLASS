marks=int(input("enter your mark:"))
if(marks>=90):
   print("grade:a")
elif(marks>=75 and marks<89):
   print("grade:b")
elif(marks>=60 and marks<74):
   print("grade:c")
elif(marks>=40 and marks<59):
   print("grade:d")
else:
   print("grade:f")