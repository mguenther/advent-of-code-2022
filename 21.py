import math
import sympy


FILENAME = '21.in'


def parse(filename):
    lines = [l.strip() for l in open(filename, 'r').readlines()]
    exprs = {}
    for line in lines:
        name = line.split(':')[0]
        expr = line.split(':')[1].strip()
        exprs[name] = expr
    return exprs


def solve(filename):

    def evaluate(name, exprs):
        expr = exprs[name]
        if not(expr.isdigit()):
            lhs, op, rhs = expr.split()
            if op == '+':
                return evaluate(lhs, exprs) + evaluate(rhs, exprs)
            elif op == '-':
                return evaluate(lhs, exprs) - evaluate(rhs, exprs)
            elif op == '*':
                return evaluate(lhs, exprs) * evaluate(rhs, exprs)
            elif op == '/':
                return evaluate(lhs, exprs) / evaluate(rhs, exprs)
        else:
            return int(expr)

    exprs = parse(filename)
    return int(evaluate('root', exprs))


def solve_for_x(filename, in_expr):

    def evaluate(name, exprs):
        expr = exprs[name]
        if isinstance(expr, sympy.Symbol):
            return expr
        if not(expr.isdigit()):
            lhs, op, rhs = expr.split()
            if name == 'root':
                return sympy.solve(evaluate(lhs, exprs) - evaluate(rhs, exprs))
            elif op == '+':
                return evaluate(lhs, exprs) + evaluate(rhs, exprs)
            elif op == '-':
                return evaluate(lhs, exprs) - evaluate(rhs, exprs)
            elif op == '*':
                return evaluate(lhs, exprs) * evaluate(rhs, exprs)
            elif op == '/':
                return evaluate(lhs, exprs) / evaluate(rhs, exprs)
        else:
            return int(expr)

    exprs = parse(filename)
    exprs[in_expr] = sympy.Symbol('x')
    return int(math.ceil(evaluate('root', exprs)[0]))


print(solve(FILENAME))
print(solve_for_x(FILENAME, 'humn'))