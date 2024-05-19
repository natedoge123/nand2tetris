import os 
import time
import sys

import functions as fnc
import read

File_Read = read.open_file(sys.argv[1])

Start_Time = time.time()

#   Do this every time
Hack_List = []
Hack_List.append("@256")
Hack_List.append("D=A")
Hack_List.append("@SP")
Hack_List.append("M=D")

Stack = []
Local = [0] * 10
Argument = [0] * 10
This = [0] * 10
That = [0] * 10
Temp_mem = [0] * 10
GP_mem = [0] * 10

S_P = 256

for line in File_Read:
    Temp = []
    Parse = line.split()

    if len(Parse) > 1:
        Area = Parse[1]
    else:
        Area = ''

    if len(Parse) > 2:
        Value = int(Parse[2])
    else:
        Value = ''

    if (Parse[0] == "push"):
        Temp = fnc.Push(S_P, Parse[1], Parse[2])
        Hack_List.extend(Temp)
        match Area:
            case "constant":
                Stack.append(Value)
            case "local":
                Stack.append(Local[Value])
            case "argument":
                Stack.append(Argument[Value])
            case "this":
                Stack.append(This[Value])
            case "that":
                Stack.append(That[Value])
            case "temp":
                Stack.append(Temp_mem[Value])

    elif (Parse[0] == "pop"):
        Temp = fnc.Pop(S_P, Parse[1], Parse[2])
        Hack_List.extend(Temp)
        match Area:
            case "local":
                Local[Value] = Stack.pop()
            case "argument":
                Argument[Value] = Stack.pop()
            case "this":
                This[Value] = Stack.pop()
            case "that":
                That[Value] = Stack.pop()
            case "static":
                Static[Value] = Stack.pop()
            case "temp":
                Temp_mem[Value] = Stack.pop()
                
    elif (Parse[0] == "add"):
        Add_1 = Stack.pop()
        Add_2 = Stack.pop()
        Temp = fnc.C_Add(S_P, Add_1, Add_2)
        Hack_List.extend(Temp)
        Stack.append(int(Add_1) + int(Add_2))

    elif (Parse[0] == "sub"):
        Sub_1 = Stack.pop()
        Sub_2 = Stack.pop()
        Temp = fnc.C_Sub(S_P, Sub_1, Sub_2)
        Hack_List.extend(Temp)
        Stack.append(int(Sub_2) - int(Sub_1))

    elif (Parse[0] == "neg"):
        Neg_1 = Stack.pop()
        Temp = fnc.C_Neg(S_P, Neg_1)
        Hack_List.extend(Temp)
        Stack.append((-Neg_1))

    elif (Parse[0] == "eq"):
        Eq_1 = Stack.pop()
        Eq_2 = Stack.pop()
        print(Eq_1, Eq_2)
        Temp = fnc.C_Eq(S_P, Eq_1, Eq_2)
        Hack_List.extend(Temp)
        Stack.append(Eq_1 == Eq_2)
        
    elif (Parse[0] == "gt"):
        Gt_1 = Stack.pop()
        Gt_2 = Stack.pop()
        print(Gt_1, Gt_2)
        Temp = fnc.C_Gt(S_P, Gt_1, Gt_2)
        Hack_List.extend(Temp)
        Stack.append(Gt_2 > Gt_1)

    elif (Parse[0] == "lt"):
        Lt_1 = Stack.pop()
        Lt_2 = Stack.pop()
        print(Lt_1, Lt_2)
        Temp = fnc.C_Lt(S_P, Lt_1, Lt_2)
        Hack_List.extend(Temp)
        Stack.append(Lt_2 < Lt_1)

    elif (Parse[0] == "and"):
        And_1 = Stack.pop()
        And_2 = Stack.pop()
        print(And_1, And_2)
        Temp = fnc.C_And(S_P, And_1, And_2)
        Hack_List.extend(Temp)
        Stack.append(int(And_1) & int(And_2))

    elif (Parse[0] == "or"):
        Or_1 = Stack.pop()
        Or_2 = Stack.pop()
        print(Or_1, Or_2)
        Temp = fnc.C_Or(S_P, Or_1, Or_2)
        Hack_List.extend(Temp)
        Stack.append(int(Or_1) | int(Or_2))

    elif (Parse[0] == "not"):
        Not_1 = Stack.pop()
        print(~Not_1)
        Temp = fnc.C_Not(S_P, Not_1)
        Hack_List.extend(Temp)
        Stack.append(~int(Not_1))

    else:
        print("it's BUSTED")

    print("~~~~~~~~~~~~~~~~~~")
    print(Parse[0], Area, Value)
    print("Stack", Stack)
    print("Local \t", Local)
    print("Arg \t", Argument)
    print("This \t", This)
    print("That \t", That)
    print("Temp \t", Temp_mem)
    print("GPR \t", GP_mem)



#print(Hack_List)
read.write(Hack_List, sys.argv[2]) 
print("Done. %s seconds" % (time.time() - Start_Time))
