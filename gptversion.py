# Define operator precedence and associativity
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L'}

# Function to perform basic arithmetic operations
def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)

# Convert infix expression to postfix using the Shunting Yard algorithm
def infix_to_postfix(expression):
    operators = []
    postfix = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = ""
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            postfix.append(float(num))
            i -= 1
        elif expression[i] in precedence:
            while (operators and operators[-1] != '(' and
                   ((associativity[expression[i]] == 'L' and precedence[expression[i]] <= precedence[operators[-1]]) or
                    (associativity[expression[i]] == 'R' and precedence[expression[i]] < precedence[operators[-1]]))):
                postfix.append(operators.pop())
            operators.append(expression[i])
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()
        i += 1
    
    while operators:
        postfix.append(operators.pop())
    
    return postfix

# Evaluate the postfix expression
def evaluate_postfix(postfix):
    values = []
    for token in postfix:
        if isinstance(token, float):
            values.append(token)
        else:
            apply_operator([token], values)
    return values[0]

# Main calculator function
def calculator():
    print("Enter a mathematical expression to calculate (e.g., 12*3+4/2+(16*16)):")
    
    while True:
        expression = input("Expression: ")
        expression = expression.replace(" ", "")  # Remove spaces
        
        try:
            postfix = infix_to_postfix(expression)
            result = evaluate_postfix(postfix)
            print(f"The result is: {result}")
        except Exception as e:
            print(f"Error: {e}")
        
        next_calculation = input("Do you want to calculate another expression? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

calculator()