import time
import sys

import functions as fnc
import read

file_read = read.open_file(sys.argv[1])
exploded_path = sys.argv[1].split('/')
static_name = exploded_path[-1].split('.')
print(static_name)

start_time = time.time()

# Preamble
hack_list = ["@256" , "D=A", "@SP", "M=D"]

# VM Memory
stack = []
local = [0] * 10
argument = [0] * 10
this = [0] * 10
that = [0] * 10
temp = [0] * 10
gpr = [0] * 10
pointer = [0] * 10
static = [0] * 10


for line in file_read:

    comm_list = []
    parse = line.split()
    command = parse[0]
    hack_list.append("// \t" + line)

    if len(parse) > 1:
        segment = parse[1]
    else:
        segment = ''

    if len(parse) > 2:
        index = int(parse[2])
    else:
        index = ''

    if (segment == ''):
        match command:
            case 'add':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Add(static_name, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 + arg_2)

            case 'sub':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Sub(static_name, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_2 - arg_1)

            case 'neg':
                arg_1 = stack.pop()
                comm_list = fnc.C_Neg(static_name, arg_1)
                hack_list.extend(comm_list)
                stack.append(-arg_1)

            case 'eq':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Eq(static_name, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 == arg_2)

            case 'lt':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Lt(static_name, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 > arg_2)

            case 'gt':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Gt(static_name, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 < arg_2)

            case 'and':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_And(static_name, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 & arg_2)

            case 'or':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Or(static_name, arg_1, arg_2)
                hack_list.extend(comm_list)
                stack.append(arg_1 | arg_2)

            case 'not':
                arg_1 = stack.pop()
                comm_list = fnc.C_Not(static_name, arg_1)
                hack_list.extend(comm_list)
                stack.append(~arg_1)

    else:
        match command:
            case "push":
                comm_list = fnc.Push(segment, index, static_name[0])
                hack_list.extend(comm_list)
                match segment:
                    case "constant":
                        stack.append(index)
                    case "local":
                        stack.append(local[index])
                    case "argument":
                        stack.append(argument[index])
                    case "this":
                        stack.append(this[index])
                    case "that":
                        stack.append(that[index])
                    case "temp":
                        stack.append(temp[index])
                    case "pointer":
                        stack.append(pointer[index])
                    case "static":
                        stack.append(static[index])


            case "pop":
                comm_list = fnc.Pop(segment, index, static_name[0])
                hack_list.extend(comm_list)
                match segment:
                    case "local":
                        local[index] = stack.pop()
                    case "argument":
                        argument[index] = stack.pop()
                    case "this":
                        this[index] = stack.pop()
                    case "that":
                        that[index] = stack.pop()
                    case "temp":
                        temp[index] = stack.pop()
                    case "pointer":
                        pointer[index] = stack.pop()
                    case "static":
                        static[index] = stack.pop()
    print(comm_list)
                        


    print(command, segment, index)
    print("stack\t", stack)
    print("local\t", local)
    print("arg\t", argument)
    print("this\t", this)
    print("that\t", that)
    print("temp\t", temp)
    print("gpr\t", gpr)
    print("pointer\t", pointer)
    print("static\t", static)
    print("<><><><><><><><>")

write_name = 1
read.write(hack_list, sys.argv[2])
print("Done. %s seconds" % (time.time() - start_time))
