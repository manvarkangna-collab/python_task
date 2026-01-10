Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #1) Print message
... print("--- 1. Print Message ---")
... print("Hello! This is a Python demonstration.")
... 
... # 2) Take two numbers from the user and print their sum
... print("\n--- 2. Sum of Two Numbers ---")
... num1 = float(input("Enter first number: "))
... num2 = float(input("Enter second number: "))
... print(f"The sum is: {num1 + num2}")
... 
... # 3) Check whether a given number is odd or even
... print("\n--- 3. Odd or Even ---")
... check_num = int(input("Enter an integer to check: "))
... if check_num % 2 == 0:
...     print(f"{check_num} is Even")
... else:
...     print(f"{check_num} is Odd")
... 
... # 4) Check whether a year is a leap year
... print("\n--- 4. Leap Year Check ---")
... year = int(input("Enter a year: "))
... if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
...     print(f"{year} is a leap year.")
... else:
...     print(f"{year} is not a leap year.")
... 
... # 5) Print Pi value
... print("\n--- 5. Pi Value ---")
... print(f"The value of Pi is: {math.pi}")
... 
... # 6) Store and print constant value
... print("\n--- 6. Constants ---")
... # In Python, we use uppercase names to indicate constants
... GRAVITY = 9.81
... print(f"The constant value of Gravity is: {GRAVITY}")
... 
... # 7) Square of a number
... print("\n--- 7. Square of a Number ---")
... sq_val = float(input("Enter number to square: "))
... print(f"The square of {sq_val} is {sq_val**2}")

# 8) Area of a circle
print("\n--- 8. Area of Circle ---")
radius = float(input("Enter radius: "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area:.2f}")

# 9) Check data type
print("\n--- 9. Data Type Check ---")
sample_var = 10.5
print(f"The data type of {sample_var} is: {type(sample_var)}")

# 10) Use math function (Example: Square root)
print("\n--- 10. Math Function (Square Root) ---")
root_num = 16
print(f"The square root of {root_num} is: {math.sqrt(root_num)}")

# 11) Find power
print("\n--- 11. Find Power ---")
base = float(input("Enter base: "))
exponent = float(input("Enter exponent: "))
print(f"{base} raised to the power of {exponent} is {pow(base, exponent)}")

# 12) Check positive or negative
print("\n--- 12. Positive or Negative ---")
val = float(input("Enter a number: "))
if val > 0:
    print("The number is Positive.")
elif val < 0:
    print("The number is Negative.")
else:
