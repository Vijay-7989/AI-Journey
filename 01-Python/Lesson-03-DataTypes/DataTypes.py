name = "Vijay"
age = 25
salary = 50000.50
is_ai_engineer = False

print(name)
print(age)
print(salary)
print(is_ai_engineer)


print(type(name))
print(type(age))
print(type(salary))
print(type(is_ai_engineer))

# print("20" + 10)
# print(10+"20")

a = [10,39]
b = a

print(id(a))
print(id(b))

print("changing b")
b.append(100)
print("b: ", b)
print("a: ", a)

print("changing a")
a.append(200)   
print("a: ", a)
print("b: ", b)


