stu={"stu":"John","section":"A","marks":85}
print(stu["stu"])
print(stu.get("section"))

for i in stu:
    print(i)
print()
for i in stu.items():
    print(i, end=" ")
print()
for i in stu.values():
    print(i)

student={
       "stu1":{"name":"11","marks":85},
       "stu2":{"name":"12","marks":90}
}

for i in student.values():
    print(i)

print(student["stu1"]["name"])