# print("Hello World")
# name = "Shahnila"
# age = 20
# print(name, age)


# a = 23
# b = 3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)
# print(a is b)
# print(a is not b)
# print(id(a))
# print(id(b))

# marks = int(input("Enter your marks: "))

# if marks >= 80:
#     print("Grade: A+")
# elif marks >= 70:
#     print("Grade: A")
# elif marks >= 60:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("Fail")


# myInput = int(input("Enter your marks: "))
# if myInput >= 90:
#     print("Grade: A+")
# elif myInput >= 80:
#     print("Grade: A")   
# elif myInput >= 70:
#     print("Grade: B")
# elif myInput >= 60:
#     print("Grade: C")   
# elif myInput >= 50:
#     print("Grade: D")
# else:    print("Fail")


# for i in range(1, 9):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)    

# for i in range(10, 0, -1):
#     print(i)

# for i in range(0, 9):
#     if i%2 != 0:
#         continue
#     print(i)

# for i in range(1, 12):
#     for j in range(1, 8):
#         print("*" * j)


# for i in range(1, 12):
#     print(f"Pyramid {i}:")
#     for j in range(1, 8):
#         print("*" * j)
#     print()  # blank line

# def multiply(a, b):
#     result = a * b
#     return result

# x = int(input("First number: "))
# y = int(input("Second number: "))

# output = multiply(x, y)
# print("Multiplication =", output)


# def add(a, b):
#     result = a + b
#     return result

# a = int(input("First number: "))
# b = int(input("Second number: "))
# output = add(a, b)
# print("Addition =", output)


# # List creation
# fruits = ["apple", "banana", "mango"]

# print(fruits)       # poori list
# print(fruits[0])    # first item
# print(fruits[2])  
# print(fruits[-1]) # last item

# # # Add item
# # fruits.append("orange")   # end me add
# # print(fruits)
# # print(fruits[-1])

# # Insert item
# fruits.insert(1, "kiwi") # index 1 pe add
# print(fruits)

# fruits.insert(-1, "grape") # index LAST pe add
# print(fruits)

# # Remove item
# fruits.remove("banana")
# print(fruits)

# # Loop through list
# for fruit in fruits:
#     print(fruit)


# # Set creation
# numbers = {1, 2, 3, 2, 4}  
# print(numbers)  # Output: {1, 2, 3, 4} → duplicate 2 remove ho gaya

# # Add item
# numbers.add(5)
# print(numbers)  # {1, 2, 3, 4, 5}

# # Remove item
# numbers.remove(3)
# print(numbers)  # {1, 2, 4, 5}

# # Loop through set
# for num in numbers:
#     print(num)


# # Dictionary creation
# student = {
#     "name": "Shahnila",
#     "age": 20,
#     "grade": "A+"
# }

# print(student)          # poori dictionary
# print(student["name"])  # access value by key

# # Add new key-value
# student["school"] = "ABC School"
# print(student)

# # Update value
# student["age"] = 21
# print(student)

# # Loop through dictionary
# for key in student:
#     print(key, "=", student[key])


# obj = {
#     "name": "Shahnila",
#     "age": 20,
#     "grade": "A+",
#     "school": "ABC School",
#     "Address": {
#         "city": "Karachi",
#         "country": "Pakistan"
#     }
# }

# print(obj["Address"]["city"])  # Output: Karachi
# obj["Address"]["city"] = "Lahore"
# print(obj["Address"]["city"])  # Output: Lahore
# obj["Address"]["Country"]= "Pakistan"
# print(obj["Address"]["Country"])  # Output: Pakistan


student1 = {"name": "Shahnila", "age": 20}

print(student1.items())
print(list("abbc"))  
# ['a', 'b', 'c']
print(set("abbc"))

