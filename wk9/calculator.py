"""
A module is a python file.
A well-developed module is a python file
where all statements are inside of functions.
A main() function: acts like starting point for the python file aka module
"""


latest_result = None  # store the value of the latest calculation

history_of_calculations = list()  # store the history of calculations

value_one = 1

def validate(num1, num2):
    return isinstance(num1, int) or isinstance(num1, float) \
and isinstance(num2, int) or isinstance(num2, float)


def record_equation(num1, num2, operator, result):
    global latest_result, history_of_calculations
    latest_result = result
    entry = {
        "operand1": num1,
        "operator": operator,
        "operand2": num2,
        "result": result
    }
    history_of_calculations.append(entry)

def add(num1, num2):
    if not validate(num1, num2):
        return None
    # result = num1 + num2 + value_one
    result = num1 + num2
    record_equation(num1, num2, "+", result)

    return result

def sub(num1, num2):
    if not validate(num1, num2):
        return None
    result = num1 - num2

    record_equation(num1, num2, "-", result)
    return result


def mul(num1, num2):
    if not validate(num1, num2):
        return None
    result = num1 * num2
    record_equation(num1, num2, "*", result)
    return result


def div(num1: float, num2: float) -> float:
    """
    This function implements the division arithmetic operation
    :param num1: first number
    :param num2: second numb
    :return: quotient value

    >>> div(10, 4)
    2.5
    >>> div(4, 0)
    4.0
    >>> div(15.0, 3.0)
    5.0
    >>> history_of_calculations[-1]['operand1']
    15.0
    >>> history_of_calculations[-1]['operand2']
    3.0
    >>> history_of_calculations[-1]['operator']
    '/'

    """
    if not validate(num1, num2):
        return 0.0
    result = num1 / (num2 if num2 > 0 else 1)
    record_equation(num1, num2, "/", result)
    return result


def main():
    print("This is a calculator module")
    print(__name__)

if __name__ == "__main__":
    main()