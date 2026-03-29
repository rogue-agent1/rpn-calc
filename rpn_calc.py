#!/usr/bin/env python3
"""rpn_calc - RPN calculator."""
import sys,argparse,json,math
OPS={"+":lambda a,b:a+b,"-":lambda a,b:a-b,"*":lambda a,b:a*b,"/":lambda a,b:a/b,"**":lambda a,b:a**b,"%":lambda a,b:a%b}
FUNCS={"sqrt":math.sqrt,"sin":math.sin,"cos":math.cos,"tan":math.tan,"log":math.log,"ln":math.log,"abs":abs,"floor":math.floor,"ceil":math.ceil}
def evaluate(tokens):
    stack=[];history=[]
    for t in tokens:
        if t in OPS:
            b,a=stack.pop(),stack.pop();r=OPS[t](a,b);stack.append(r)
            history.append({"op":t,"args":[a,b],"result":r})
        elif t in FUNCS:
            a=stack.pop();r=FUNCS[t](a);stack.append(r)
            history.append({"op":t,"args":[a],"result":r})
        elif t=="pi":stack.append(math.pi)
        elif t=="e":stack.append(math.e)
        else:stack.append(float(t))
    return stack,history
def main():
    p=argparse.ArgumentParser(description="RPN calculator")
    p.add_argument("expression",nargs="+")
    p.add_argument("--verbose",action="store_true")
    args=p.parse_args()
    stack,history=evaluate(args.expression)
    result={"result":stack[-1] if stack else None,"stack":stack}
    if args.verbose:result["history"]=history
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
