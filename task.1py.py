Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # 1. Take input from users
... name = input("Enter your name: ")
... num1 = float(input("Enter first number: "))
... num2 = float(input("Enter second number: "))
... num3 = float(input("Enter third number: "))
... 
... # 2. Print a welcome message
... print(f"\nWelcome, {name}!")
... 
... # 3. Calculate Simple Interest (Formula: P*R*T / 100)
... # Let's assume the inputs are Principal, Rate, and Time
... p, r, t = 1000, 5, 2
... simple_interest = (p * r * t) / 100
... print(f"Simple Interest on $1000 at 5% for 2 years: {simple_interest}")
... 
... # 4. Find maximum of 2 numbers
... maximum = max(num1, num2)
... print(f"The maximum of {num1} and {num2} is: {maximum}")
... 
... # 5. Print numbers 1 to 5
... print("Numbers 1 to 5:")
... for i in range(1, 6):
...     print(i, end=" ")
... print() # New line
... 
... # 6. Find length of a string
... text = "Python Programming"
... print(f"The length of '{text}' is: {len(text)}")
... 
... # 7. Print 1st character of a string
... print(f"The first character is: {text[0]}")
... 
... # 8. Print last character of a string
... print(f"The last character is: {text[-1]}")
... 
... # 9. Check positive or negative numbers
... check_num = float(input("Enter a number to check if positive/negative: "))
... if check_num > 0:
...     print("The number is Positive.")
... elif check_num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# 10. Add 3 numbers
total = num1 + num2 + num3
