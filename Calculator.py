num1 = input("Enter your first number:\n")
operator = (input("Operator (+, -, *, /,:\n")
num2 = input("Enter your second number:\n")

out = None

if operator =="+":
    out = num1 + num2
elif operator == "-":
    out= num1 - num2
elif operator =="*":
    out = num1 * num2
elif operator =="/":
    out = num1 / num2

print("Answer: " + str(out))




