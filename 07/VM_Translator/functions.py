def Push(Segment, Index, file_name):
    Instr = []
    match Segment:
        case "constant":
            Index = str(Index)
            Instr.append("@" + Index)
            Instr.append("D=A")
            
        case "temp":
            Index = str(5 + int(Index))
            Instr.append("@R" + str(Index))
            Instr.append("D=M")

        case "gpr":
            Index = str(13 + int(Index))
            Instr.append("@R" + str(Index))
            Instr.append("D=M")

        case "pointer":
            seg_base = Seg_Switcher(Segment)
            this_or_that = seg_base + Index
            Instr.append("@R" + str(this_or_that))
            Instr.append("D=M")

        case "static":
            static = file_name + '.'+ str(Index)
            Instr.append("@" + str(static))
            Instr.append("D=M")

        case _:
            seg_base = Seg_Switcher(Segment)
            Instr.append("@" + str(seg_base))
            Instr.append("D=M")
            Instr.append("@" + str(Index))
            Instr.append("A=D+A")
            Instr.append("D=M")

    Instr.append("@SP")
    Instr.append("A=M")
    Instr.append("M=D")
    Instr.append("@SP")
    Instr.append("M=M+1")

    return Instr

def Pop(Segment, Index, file_name):
    Instr = []

    Instr.append("@SP")
    Instr.append("M=M-1")
    Instr.append("A=M")
    Instr.append("D=M") # Now the last value in the stack is in D

    match Segment:
        case "temp":
            seg_base = Seg_Switcher(Segment)
            tempp = str(seg_base + Index)
            Instr.append("@R" + str(tempp))
            Instr.append("M=D")

        case "gpr":
            seg_base = Seg_Switcher(Segment)
            gpr = str(seg_base + int(Index))
            Instr.append("@R" + str(gpr))
            Instr.append("M=D")

        case "pointer":
            seg_base = Seg_Switcher(Segment)
            pointerr = str(seg_base + int(Index))
            Instr.append("@R" + str(pointerr))
            Instr.append("M=D")

        case "static":
            static = file_name + '.' + str(Index)
            Instr.append("@" + str(static))
            Instr.append("M=D")

        case _:
            seg_base = Seg_Switcher(Segment)
            Instr.append("@R13")
            Instr.append("M=D") #last item from stack stored in gpr1
            Instr.append("@" + str(seg_base))
            Instr.append("D=M")
            Instr.append("@" + str(Index))
            Instr.append("D=D+A")
            Instr.append("@R14")
            Instr.append("M=D") #address to store is now at r14
            Instr.append("@R13")
            Instr.append("D=M")
            Instr.append("@R14")
            Instr.append("A=M")
            Instr.append("M=D")

    return Instr

def C_Add(file_name, Val1, Val2):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D+M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Sub(file_name, Val1, Val2):  # Val1 - Val2
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D-M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Neg(file_name, Val1):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.append("@R13")
    Instr.append("D=0")
    Instr.append("M=D-M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr
 
def C_Eq(file_name, Val1, Val2):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    if (Val1 == Val2):  # "-1" is true and "0" is false
        Instr.extend(C_True(file_name))
    else:
        Instr.extend(Push("constant", 0, file_name))

    return Instr

def C_Lt(file_name, Val1, Val2):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    if (Val2 < Val1):  # "-1" is true and "0" is false
        Instr.extend(C_True(file_name))
    else:
        Instr.extend(Push("constant", 0, file_name))

    return Instr

def C_Gt(file_name, Val1, Val2):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    if (Val2 > Val1):  # "-1" is true and "0" is false
        Instr.extend(C_True(file_name))
    else:
        Instr.extend(Push("constant", 0, file_name))

    return Instr

def C_And(file_name, Val1, Val2):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D&M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Or(file_name, Val1, Val2):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D|M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Not(file_name, Val1):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.append("@R13")
    Instr.append("M=!M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_True(file_name):
    Instr = []
    Instr.extend(Push("constant", 0, file_name))
    Instr.extend(Push("constant", 1, file_name))
    Instr.extend(C_Sub(S_P, 0, 1))

    return Instr

def Seg_Switcher(segment):
    base = 0
    match segment:
        case "local":
            base = 1
        case "argument":
            base = 2
        case "this":
            base = 3
        case "that":
            base = 4
        case "gpr":
            base = 13
        case "pointer":
            base = 3
        case "static":
            base = 16
    return base

