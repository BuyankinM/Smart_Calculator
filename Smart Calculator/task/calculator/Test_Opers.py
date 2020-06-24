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
            stack.append(int(val_op))
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


prior = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}

oper_str = "2*(3+4)+1"
oper_str = "3+8*((4+3)*2+1)-6/(2+1)"
oper_str = "1 +++ 2 * 3 -- 4"
# oper_str = "-5 / -2"

postfix_operations = transform_infix_to_postfix(oper_str)

if postfix_operations is None or "(" in postfix_operations or ")" in postfix_operations:
    print("Invalid expression")
else:
    print(postfix_operations)
    res = calc_postfix(postfix_operations)
    print(res)
