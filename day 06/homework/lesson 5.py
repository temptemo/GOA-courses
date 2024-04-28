print(5 > 6 or 10 < 11)  # True
print(3 == 4 or 7 > 8)  # False
print(20 < 15 or 9 == 9) # True
print(100 > 101 or 50 == 50) # True
print(2 > 3 or 6 < 4) # False

#2
print(5 > 6 and 10 < 11)  # False
print(3 == 4 and 7 > 8)  # False
print(20 < 15 and 9 == 9) # False
print(100 > 101 and 50 == 50) # False
print(2 > 1 and 6 < 8) # True


#3
#and operator
variable_and = (5>4) and (10<27) #True because both conditions are True
# or operator
variable_or = (5<3) or (10<20) #True because onme of the conditions True
#comparing variables
print(variable_and)
print(variable_or)

#4
variable1 =int(input("Write First Number"))
variable2 =int(input("write second Number"))

compare_and = (variable1 < 10) and (variable2 > 3)
compare_or = (variable1 > 123 ) or (variable2 < 34)

print(compare_and,compare_or)

#5
variable1 = 10 < 20
variable2 = 5 == 5

variable3 = variable1  > variable2
print("result:", variable3)

# 2 part of Homework
#1
var1 = 10
var2 = "Goa Best"
var3 =10.3
var4 = True
print(type(var1), type(var2), type(var3), type(var4))

#2
username = input("Enter Your name :")
group_member = input("Enter Your Group Number: ")

print(" Hello Chad " + " " + username + " "  " Welcome to Group " + " " + group_member)

#3
number1 = 20
number2 = 4
result = number1 / number2

print("Result ", result)
print("Type of Result", type(result)) 

#4
num1 = 20 
num2  = 24

print(str(num1) + str(num2))

#5
nume1 = 4.12
nume2 = 7.19
nume3 = 34.3
nume4 = 1032.45
nume5 =1.5

print(nume1, int(nume1))
print(nume2, int(nume2))
print(nume3, int(nume3))
print(nume4, int(nume4))
print(nume5, int(nume5))