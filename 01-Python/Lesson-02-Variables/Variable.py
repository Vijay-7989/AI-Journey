name = "vijay"
age = 25
city = "chenani"
company = "LTIM"
experience = 1.3

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Company:", company)
print("Experience:", experience, "years")

another_name = name

another_name= "kumar"

print(id(name))
print(id(another_name))

print(id(name) == id(another_name))

# print(id(age))
# print(id(city))
# print(id(company))
# print(id(experience))


name = "kumar"
print("updated name:", name)

print()
print("on strings")
a = "vijay"
b = a
b = b+" kumar"
print("a:", a)
print("b:", b)

print()
print("on lists")
a = [10, 20, 30]
b = a
b.append(40)
print("a:", a)
print("b:", b)