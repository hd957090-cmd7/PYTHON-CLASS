str = "formula 1 car"
print(len(str))

print(str.upper())

print(str.lower())

print(str.capitalize())

x = str.find("o")
print(x)

q = str.replace("1", "one")
print(q)

str1 = "select a language"
for i in str1:
    print(i)

str2 = "select a language"
for j in str2:
    if(j.isupper()):
        print(j.lower())
    else:
        print(j.upper())