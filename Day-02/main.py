# name = "kunal"
# height = 32.5
# age = 21


# print(type(name))
# print(name)


# print(type(height))
# print(height)

# print(type(age))
# print(age)



# lenght = input("enter the lenght")
# width = input("enter width")

# area = int(lenght) * int(width)
# print(area)



# C = input("entwr temprature")

# F = (int(C) * 9 // 5) +32

# print(F)



# N = int(input("enter no"))

# if N % 2 == 0:
#     print("even")
# else : 
#     print("Odd")


# Calculator 


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice: ")

if choice == "1":
    result = num1 + num2

elif choice == "2":
    result = num1 - num2

elif choice == "3":
    result = num1 * num2

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid operation"

print("Result:", result)