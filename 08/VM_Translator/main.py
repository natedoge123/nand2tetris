import time
import sys

import functions as fnc
import read

#file_read = read.open_file(sys.argv[1])
file_read = read.open_dir(sys.argv[1])
exploded_path = sys.argv[1].split('/')
save_name = exploded_path[-2]
sys_init_call = ['call Sys.init 0']
file_read = sys_init_call + file_read

start_time = time.time()
hack_list = []
equal_count = 1
less_count = 1
great_count = 1
call_count = 1
static_count = 1


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
    parse = line.split('/')[0]
    parse = parse.split()

    if '~' in line:
        static_name = line[line.find('~')+1:]
    
    if len(parse) > 0:
        command = parse[0]
    else:
        continue

    hack_list.append("// \t" + line)

    if len(parse) > 1:
        segment = parse[1]
    else:
        segment = ''

    if len(parse) > 2:
        index = parse[2]
    else:
        index = ''

    if (segment == ''):
        match command:
            case 'add':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Add(static_name)
                hack_list.extend(comm_list)
                stack.append(arg_1 + arg_2)

            case 'sub':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Sub(static_name)
                hack_list.extend(comm_list)
                stack.append(arg_2 - arg_1)

            case 'neg':
                arg_1 = stack.pop()
                comm_list = fnc.C_Neg(static_name)
                hack_list.extend(comm_list)
                stack.append(-arg_1)

            case 'eq':
                equal_count += 1
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Eq(static_name, equal_count)
                hack_list.extend(comm_list)
                stack.append(arg_1 == arg_2)

            case 'lt':
                less_count += 1
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Lt(static_name, less_count)
                hack_list.extend(comm_list)
                stack.append(arg_1 > arg_2)

            case 'gt':
                great_count += 1
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Gt(static_name, great_count)
                hack_list.extend(comm_list)
                stack.append(arg_1 < arg_2)

            case 'and':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_And(static_name)
                hack_list.extend(comm_list)
                stack.append(arg_1 & arg_2)

            case 'or':
                arg_1 = stack.pop()
                arg_2 = stack.pop()
                comm_list = fnc.C_Or(static_name)
                hack_list.extend(comm_list)
                stack.append(arg_1 | arg_2)

            case 'not':
                arg_1 = stack.pop()
                comm_list = fnc.C_Not(static_name)
                hack_list.extend(comm_list)
                stack.append(~arg_1)

            case 'return':
                comm_list = fnc.return_gen()
                hack_list.extend(comm_list)

            case _:
                print("skip math")

    else:
        match command:
            case "push":
                index = int(parse[2])
                comm_list = fnc.Push(segment, index, static_name)
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
                try: 
                    temp_pop_val = stack.pop()
                except IndexError:
                    print('oopsie')

                index = int(parse[2])
                comm_list = fnc.Pop(segment, index, static_name)
                hack_list.extend(comm_list)
                match segment:
                    case "local":
                        local[index] = temp_pop_val
                    case "argument":
                        argument[index] = temp_pop_val
                    case "this":
                        this[index] = temp_pop_val
                    case "that":
                        that[index] = temp_pop_val
                    case "temp":
                        temp[index] = temp_pop_val
                    case "pointer":
                        pointer[index] = temp_pop_val
                    case "static":
                        static[index] = temp_pop_val
                        
            case "label":
                comm_list = "(" + segment + ")"
                hack_list.append(comm_list)

            case "goto":
                comm_list.append(("@" + segment))
                comm_list.append("0;JMP")
                hack_list.extend(comm_list)

            case "if-goto":
                comm_list = fnc.if_goto(segment, static_name)
                hack_list.extend(comm_list)

            case "function":
                comm_list = fnc.fucntion_gen(segment, index)
                hack_list.extend(comm_list)

            case "call":
                comm_list = fnc.call_gen(segment, index,  call_count)
                hack_list.extend(comm_list)
                call_count += 1

            case _:
                print("skip command")


    print(comm_list)
                        


    print(command, segment, index)
    print("stack\t", stack)
    #print("local\t", local)
    #print("arg\t", argument)
    #print("this\t", this)
    #print("that\t", that)
    #print("temp\t", temp)
    #print("gpr\t", gpr)
    #print("pointer\t", pointer)
    #print("static\t", static)
    print("<><><><><><><><>")

write_name = sys.argv[1] + save_name
print(write_name)



read.write(hack_list, write_name )
print("Done. %s seconds" % (time.time() - start_time))
