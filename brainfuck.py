#!/usr/bin/python3

import sys

def skip_loop(code, i):
    loop = 1
    lc = len(code)
    while loop > 0 and i < lc:
        if code[i] == "[":
            loop += 1
        elif code[i] == "]":
            loop -= 1
        i += 1
    return i - 1

def interpret_brainfuck(code, buffer_size=30000):
    buffer = [0] * buffer_size
    loop_stack = []
    pos = 0
    lc = len(code)
    i = 0
    while i < lc:
        if code[i] == "+" :
            buffer[pos] += 1
        elif code[i] == "-":
            buffer[pos] -= 1
        elif code[i] == ">":
            pos += 1
        elif code[i] == "<":
            pos -=1
        elif code[i] == ".":
            sys.stdout.write(chr(buffer[pos]))
        elif code[i] == ",":
            buffer[pos] = ord(sys.stdin.read(1))
        elif code[i] == "[":
            if buffer[pos] != 0:
                if i - 1 not in loop_stack:
                    loop_stack.append(i - 1)
            else :
                i = skip_loop(code, i + 1)
                loop_stack.pop(-1)
        elif code[i] == "]":
            i = loop_stack[-1]
        i += 1

def main(args):
    code = None
    # first we bufferize all the code
    with open(args[0], "r") as f:
        code = f.read()
    if len(args) == 2:
        interpret_brainfuck(code, int(args[1]))
    else:
        interpret_brainfuck(code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("Please enter a file to interpret as argument")
