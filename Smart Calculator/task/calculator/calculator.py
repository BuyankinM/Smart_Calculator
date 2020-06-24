from string import ascii_letters, digits
from collections import deque
import re


def pack_operations(op):
    op = re.sub(r"([-+*/()])", r" \1 ", op)

    res_op = []
    operations_cumulative = ""
    minus_op = ["*", "-1"]

    for symbol in op.split():
        is_minus = False

        if symbol in "*/+-":
            operations_cumulative += symbol
        else:
            if operations_cumulative:
                if set(operations_cumulative) == set("+-") \
                        or set(operations_cumulative) == set("+") \
                        or set(operations_cumulative) == set("-"):

                    operation = "-" if operations_cumulative.count("-") % 2 else "+"
                    if not res_op and operation == "-":
                        # first minus
                        is_minus = True

                else:
                    if len(operations_cumulative) > 1 and operations_cumulative.endswith("-"):
                        # may be *- or /-
                        is_minus = True
                        operations_cumulative = operations_cumulative[:-1]

                    if len(operations_cumulative) == 1:
                        operation = operations_cumulative
                    else:
                        return None

                if not is_minus or operation != "-":
                    res_op.append(operation)

            res_op.append(symbol)

            if is_minus:
                res_op.extend(minus_op)

            operations_cumulative = ""

    return res_op


def transform_infix_to_postfix(op):
    list_ops = pack_operations(op)
    if list_ops is None:
        return None

    stack = deque()
    result_operations = []

    for symbol in list_ops:

        if symbol not in prior:

            result_operations.append(symbol)

        elif not stack:

            stack.append(symbol)

        elif symbol == ")":

            while stack:
                if stack[-1] == "(":
                    stack.pop()  # del first (
                    break

                result_operations.append(stack.pop())
            else:
                return None

        elif stack[-1] == "(" or symbol == "(":

            stack.append(symbol)

        elif prior[symbol] > prior[stack[-1]]:

            stack.append(symbol)

        elif prior[symbol] <= prior[stack[-1]]:

            while stack and (stack[-1] != "(" or prior[symbol] <= prior[stack[-1]]):
                result_operations.append(stack.pop())

            stack.append(symbol)

    while stack:
        result_operations.append(stack.pop())

    return result_operations


def calc_postfix(op):
    stack = deque()

    for val_op in op:

        if val_op not in prior:
            if re.fullmatch(r"-?\d+", val_op):
                value = int(val_op)
            else:
                value = my_calc_vars[val_op]
            stack.append(value)

        elif len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()

            if val_op == "+":
                stack.append(a + b)
            elif val_op == "-":
                stack.append(a - b)
            elif val_op == "*":
                stack.append(a * b)
            elif val_op == "/":
                stack.append(a / b)
        elif val_op == "-":
            stack.append(stack.pop() * -1)

    return stack.pop()


def calc_res(user_inp):
    list_ops = user_inp.split()
    res = 0
    op = "+"
    inv_exp = False

    for val in list_ops:
        is_num_var = val.replace("-", "").replace("+", "")
        if is_num_var:
            try:
                if val.strip(digits) == "":
                    value = val
                else:
                    value = my_calc_vars[val]

                res = res + int(value) * (-1) ** (op.count("-"))
            except ValueError:
                inv_exp = True
                break
            op = ""
        else:
            op += val
    if op or inv_exp:
        res = "Invalid expression"
    return res


def set_var(user_inp: str):
    left_part, right_part = [part.strip() for part in user_inp.split("=", 1)]
    right_part_is_var = (right_part.strip(ascii_letters) == "")
    right_part_is_dig = (right_part.strip(digits) == "")

    if left_part.strip(ascii_letters):
        print("Invalid identifier")
    elif not right_part_is_var and not right_part_is_dig:
        print("Invalid assignment")
    elif right_part_is_var and right_part not in my_calc_vars:
        print("Unknown variable")
    elif right_part_is_var:
        my_calc_vars[left_part] = my_calc_vars[right_part]
    else:
        my_calc_vars[left_part] = int(right_part)


def print_var(var_name: str):
    if var_name.strip(ascii_letters):
        print("Invalid identifier")
    elif var_name not in my_calc_vars:
        print("Unknown variable")
    else:
        print(my_calc_vars[var_name])


my_calc_vars = {}
prior = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}

while True:
    user_input = input().strip()

    if not user_input:
        continue
    elif user_input.startswith("/"):
        if user_input == "/exit":
            print("Bye!")
            break
        elif user_input == "/help":
            print("The program calculates the sum and subtraction of numbers")
        else:
            print("Unknown command")
    elif "=" in user_input:
        set_var(user_input)
    elif not re.findall(r"[-+*/()]", user_input):
        print_var(user_input)
    elif user_input:
        postfix_operations = transform_infix_to_postfix(user_input)
        if postfix_operations is None or "(" in postfix_operations or ")" in postfix_operations:
            print("Invalid expression")
        else:
            result = calc_postfix(postfix_operations)
            print(int(result))
