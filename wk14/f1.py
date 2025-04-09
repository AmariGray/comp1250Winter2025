"""
low-level AI talking/assistance 

1) prompt to do something
2) prompt is parsed to send back output

Phase 1
allow user to prompt
output what user inputted

Phase 2
allow math caculations

number  *-/x+ number

what is , result
"""
import re

def do_calculation(num1, num2, operator):
        
    calculation = num1 + num2
    
    if operator in ['x', '*']:
        calculation = num1 * num2
    elif operator == "-":
        calculation = num1 - num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        calculation = num1 / num2
    elif operator == "^":
        calculation = num1 ** num2
    return True, f"{num1} {operator} {num2} = {calculation}"
"""
    else:
        return False, "Could not compute arithmetic request"
"""        
def is_arithmetic_request(prompt):
    # are there two numbers in the prompt?
    regex_numbers = r"[-+]?\d+"
    result =re.findall(string=prompt, pattern=regex_numbers)
    print(result)
    regex_symbols = r"[x\/\*\+\-\^]"
    result1 =re.findall(string=prompt, pattern=regex_symbols)
    print(result1)
    s1 = set(result1)
    s1.difference_update(set(result))
    print(s1)
    l1 = list(s1)
    for value in result:
        # determine if first char is a symbol
        first_char = value[0]
        if not first_char.isdigit() and first_char in l1:
            l1.remove(first_char)
    print(l1)
    
    if len(result) >= 2 and len(l1) >= 1:
        index = 0
        final_result = 0
        while index < len(result):
            num1 = int(result[index])
            num2 = int(result[index + 1])
            operator = l1[index]
            index += 1
            
            final_result += do_calculation(num1, num2, operator)[1]
        
       
    return True
while True:
    prompt = input("Say something. Type quit to exit: ").lower()
    if prompt[0] == 'q':
        break
    # print("You inputted", prompt)
    valid, result = is_arithmetic_request(prompt)
    print(result)

# how do we allow multiple arithmic equations
    
    
