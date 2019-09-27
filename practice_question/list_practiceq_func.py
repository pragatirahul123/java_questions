def calc(num1, num2, operator):
    if operator == '+':
        return a + b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '-':
        return a - b
    elif operator =='%':
        return a%b
user1=raw_input("enter a operator")
if chr(42<=47):
    print(calc(5,10,user1))
    
