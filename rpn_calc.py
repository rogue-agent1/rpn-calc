#!/usr/bin/env python3
"""Reverse Polish Notation (RPN) calculator."""
import sys, math, operator

OPS = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv,
       '//':operator.floordiv, '%':operator.mod, '**':operator.pow,
       'sqrt':lambda s: [math.sqrt(s.pop())], 'sin':lambda s: [math.sin(s.pop())],
       'cos':lambda s: [math.cos(s.pop())], 'abs':lambda s: [abs(s.pop())],
       'swap':lambda s: [s[-1], s[-2]] if len(s)>=2 else s, 'dup':lambda s: [s[-1], s[-1]]}

def evaluate(expr):
    stack = []
    for token in expr.split():
        if token in OPS:
            op = OPS[token]
            if callable(op) and token in ('sqrt','sin','cos','abs'):
                result = op(stack)
                stack.extend(result)
            elif token == 'swap':
                if len(stack) >= 2: stack[-1], stack[-2] = stack[-2], stack[-1]
            elif token == 'dup':
                stack.append(stack[-1])
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(op(a, b))
        else:
            stack.append(float(token))
    return stack[-1] if stack else 0

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(evaluate(' '.join(sys.argv[1:])))
    else:
        print("RPN Calculator (Ctrl+D to quit)")
        stack = []
        while True:
            try:
                line = input('> ')
                print(evaluate(line))
            except EOFError:
                break
