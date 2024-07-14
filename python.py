name = input("Please enter your name: ")
age = input("Enter your age: ")
marks = input("Enter your marks: ")

print("Welcome to my page., ", name)
print("You are", age , ("years old."))
print("Your marks are:", marks , ("Good Marks"))
print("You are intelligent", name)
first = int(input("Enter first value : "))
second = int(input("Enter second value :"))

print("sum =", first + second)

side = float(input("Enter square side :"))

print("Area of square = ", side * side)

a = float(input("Enter first floating value : "))
b = float(input("Enter second floating value : "))

print("Ans =", (a+b)/2)

a = int(input("Enter frst number : "))
b = int(input("Enter second number : "))

print(a >= b)

length = int(input("Enter length of rectangle: "))
height = int(input("Enter height rectangle: "))
perimeter = (length + height) * 2
print("Perimeter of rectangle :", perimeter)

a = float(input("Enter a random number: "))
b = float(input("Enter second random number: "))
print("Answer = ", a==b)

age = int(input("Enter your age: "))


if(age == 18):
    print("You can drive a car next year")


elif(age <= 5):
    print("You are a baby age", age,"is not valid")

elif(age >= 110):
    print("You are a bot")

elif(age >= 18 and age <= 100):
    print("You can dive a car because your age is", age,)



elif(age <= 18):
    print("Sorry, You cannot drive a car because your age is", age,)

else:
    print("You cannot proceed")
