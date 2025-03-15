#  Swap Two Numbers Without Using a Third Variable
a = 5
b = 10
print ("a = ", a , "and ",  "b = ", b )
a,b = b,a
print("a = ", a, "b = ", b)




# Now take user input instead of fixed values
a = float(input("Enter a: "))
b = float(input("Enter b: "))
a,b = b,a
print(" After Swapping, a = ", a, "and b = ", b)





# Reverse a number without using string
num = int(input("Enter a number: "))
rev = 0
while num > 0: # the loop runs until we have digits left in our number
    rev = (rev * 10) + (num % 10) # by (num % 10) we get last digit (4) and we have to add this in (rev *10) i.e (0)
    num =(num // 10) # as we have got last number above so here we will remove it and number becomes 123
                     #  now again loop runs and check num>0 
                     #                               123 > 0     True
                     #                               rev = (4*10) + (123 % 10)        // 40 + 3 = 43
                     #  now remove last digit        num = (123 // 10)                //  12
                     #  again loop runs because      12 > 0       True
                     #                               rev = (43 *10) + (12 % 10)        // 430 + 2 = 432
                     #  now remove last digit        num = (12 // 10)                  // 1
                     #  now again loop runs           1>0           True
                     #                               rev = (432 * 10) + (1 % 10)        //4320 + 1 = 4321
                     #  now remove last digit        num = num // 10                     //0
                     #  now loop stops because num is not equal to 0
print("Reverse number is: ", rev)    


#Reverse a value
user = input("Enter a value in order to reverse ")
a = user[::-1]
print("Reverse value is: ", a)







#Check whether the input value(numbers / string) is palindrome

user_input = input("Enter a value to check whether a vulue is palindrome or not? : ")
if user_input== user_input[::-1]:
    print (f"{user_input} is palindrome")
else:
    print(f"{user_input} is not palindrome")


#Check whether a number is even / odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# Check Even / Odd for list of numbers
numbers = [21,18,32,45,78,25] #list of numbers
for num in  numbers: #iterate through the list
    if num % 2 == 0:
        print(f"Even :{num}")
    else:
        print(f"Odd: {num}")


#User Input for multiple numbers to check even and odd
user_input = input("Enter numbers separated by spaces: ")
input_list = user_input.split() # separate by space
number = [int(num) for num in input_list]
for num in number:
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")



# Max split example
text = "1, 2, 3, 4, 5, 6, 7, 8, 9"
a = text.split(', ', 4)
print(a)




# #Sum of digits of a number without using strings
num = int(input("Enter a number: "))
sum = 0
while num>0:
    sum = sum + num%10
    num = num //10
print("Sum of digit: ", sum)


# Sum of digits of a number with strings
num = input("Enter a number: ")
sum_of_digits = sum(int(digits) for digits in num)
print("Sum of digits: ", sum_of_digits)


num = input("Enter your number: ")
if num.isdigit():
    sum_of_digits = sum(int(digit) for digit in num)
    print("Sum of Digits: ", sum_of_digits)
else:
    print("Invalid Input, Please input a valid number ")


# Swapping numbers using third variable
a=5
b=10
print(f"Before Swapping a= {a} and b= {b}")
temp = a
a=b
b=temp
print(f"After Swapping a= {a} and b={b} ")



name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, My name is {name} and I'm {age} years old!")

num1 =float(input("Enter first number: "))
num2 =float(input("Enter second number: "))
print(num1 + num2)

a= 10
b=2
print(f"Before Swapping: a={a} and b={b}")
temp = a
a=b
b=temp
print(f"After Swapping: a={a} and b={b}")

num = int(input("Enter a number: "))
square = num**2
cube = num**3
print(f"Suare: {square} \nCube: {cube}")

temp = float(input("Enter temperature in celsius: "))
farenheit = (temp * 9/5) +32
print("Temperature in Farenheit is: ", farenheit)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
remainder = a-(a//b)*b
print("Remainder: ", remainder)


