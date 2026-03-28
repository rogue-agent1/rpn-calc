#!/usr/bin/env python3
"""rpn_calc - Reverse Polish Notation (RPN) calculator."""
import sys, math, operator

OPS = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv,
       '//':operator.floordiv, '%':operator.mod, '**':operator.pow, '^':operator.pow,
       'sqrt':lambda a: math.sqrt(a), 'sin':math.sin, 'cos':math.cos, 'tan':math.tan,
       'log':math.log, 'log2':math.log2, 'log10':math.log10, 'abs':abs,
       'min':min, 'max':max, 'floor':math.floor, 'ceil':math.ceil}
UNARY = {'sqrt','sin','cos','tan','log','log2','log10','abs','floor','ceil'}
CONSTS = {'pi':math.pi, 'e':math.e, 'tau':math.tau}

def evaluate(tokens):
    stack = []
    for tok in tokens:
        if tok in CONSTS: stack.append(CONSTS[tok])
        elif tok in OPS:
            if tok in UNARY:
                a = stack.pop(); stack.append(OPS[tok](a))
            else:
                b, a = stack.pop(), stack.pop(); stack.append(OPS[tok](a, b))
        else:
            try: stack.append(float(tok))
            except: print(f"Unknown: {tok}"); return None
    return stack[-1] if stack else None

def interactive():
    print("RPN Calculator (type 'q' to quit)")
    stack = []
    while True:
        try: line = input('> ')
        except: break
        if line.strip() in ('q','quit'): break
        if line.strip() == 'stack': print(f"  {stack}"); continue
        if line.strip() == 'clear': stack.clear(); continue
        result = evaluate(line.split())
        if result is not None: print(f"  = {result}")

def main():
    args = sys.argv[1:]
    if not args or args[0] == '-i': interactive()
    elif '-h' in args:
        print("Usage: rpn_calc.py EXPR | rpn_calc.py -i\n  rpn_calc.py 3 4 + 2 *"); return
    else:
        result = evaluate(args)
        if result is not None: print(result)

if __name__ == '__main__': main()
