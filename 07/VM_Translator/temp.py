import os
import time
import sys

import functions as fnc
import read

file_read = read.open_file(sys.argv[1])

start_time = time.time()

# Preamble
hack_list = []
hack_list.append("@256" , "D=A", "@SP", "M=D")

# VM Memory
stack = []
local = [0] * 10
argument = [0] * 10
this = [0] * 10
that = [0] * 10
temp = [0] * 10
gpr = [0] * 10

s_p = 256

for line in file_read:

    comm_list = []
    parse = line.split()
    command = parse[0]

    if len(parse) > 1:
        segment = parse[1]
    else:
        segment = ''

    if len(parse > 2:
        index = int(parse[2])
    else:
        index = ''

    if (segment == ''):
        match command:
            case 'add':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Add(s_p, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 + arg_2)
            case 'sub':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Sub(s_p, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 + arg_2)
            case 'neg':
                arg_1 = stack.pop()
                comm_list = fnc.C_Neg(S_P, arg_1)
                hack_list.extend(comm_list)
                stack.append(-arg_1)
            case 'eq':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Eq(s_p, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 == arg_2)
            case 'lt':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Lt(s_p, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 > arg_2)
            case 'gt':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Gt(s_p, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 < arg_2)
            case 'and':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_And(s_p, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 & arg_2)
            case 'or':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Or(s_p, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 | arg_2)
            case 'not':
                arg_1 = stack.pop()
                comm_list = fnc.C_Not(s_p, arg_1)
                hack_list.extend(comm_list)
                stack.append(~arg_1)
    else:
        match command:
            case "push":

            case "pop":



                    


        print("<><><><><><><><>")
        print(command, segment, index)
        print("stack \t", stack)
        print("local \t", local)
        print("arg \t", arg)
        print("this \t", this)
        print("that \t", that)
        print("temp \t", temp)
        print("gpr \t", gpr)


    read.write(hack_list, sys.argv[2])
    print("Done. %s seconds" % (time.time() - start_time))
