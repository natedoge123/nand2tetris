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

def C_Add(file_name):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D+M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Sub(file_name):  # Val1 - Val2
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D-M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Neg(file_name):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.append("@R13")
    Instr.append("D=0")
    Instr.append("M=D-M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr
 
def C_Eq(file_name, count):
    count = str(count)
    Instr = []
    Instr.extend(C_Sub(''))

    Instr.extend(Pop("gpr", 0 , file_name))

    Instr.append("@R13")
    Instr.append("D=M")

    Instr.append("@EQUAL" + count)
    Instr.append("D;JEQ")

    Instr.append("@UNEQUAL" + count)
    Instr.append("0;JMP")

    Instr.append('(EQUAL' + count + ')')
    Instr.extend(C_True(file_name))
    Instr.append("@END_EQ" + count)
    Instr.append("0;JMP")

    Instr.append('(UNEQUAL' + count + ')')
    Instr.extend(Push("constant", 0, file_name))

    Instr.append('(END_EQ' + count + ')')

    return Instr

def C_Lt(file_name, count):
    count = str(count)
    Instr = []

    Instr.extend(C_Sub(''))

    Instr.extend(Pop("gpr", 0 , file_name))

    Instr.append("@R13")
    Instr.append("D=M")

    Instr.append("@LESS" + count)
    Instr.append("D;JLT")

    Instr.append("@NOTLESS" + count)
    Instr.append("0;JMP")

    Instr.append("(LESS" + count + ")")
    Instr.extend(C_True(file_name))
    Instr.append("@END_LESS" + count)
    Instr.append("0;JMP")

    Instr.append("(NOTLESS" + count + ")")
    Instr.extend(Push("constant", 0, file_name))
    
    Instr.append("(END_LESS" + count +")")

    return Instr


def C_Gt(file_name, count):
    count = str(count)
    Instr = []
 
    Instr.extend(C_Sub(''))

    Instr.extend(Pop("gpr", 0 , file_name))

    Instr.append("@R13")
    Instr.append("D=M")

    Instr.append("@GREAT" + count)
    Instr.append("D;JGT")

    Instr.append("@NOTGREAT" + count)
    Instr.append("0;JMP")

    Instr.append("(GREAT" + count + ")")
    Instr.extend(C_True(file_name))
    Instr.append("@END_GREAT" + count)
    Instr.append("0;JMP")

    Instr.append("(NOTGREAT" + count + ")")
    Instr.extend(Push("constant", 0, file_name))
    
    Instr.append("(END_GREAT" + count + ")")

    return Instr

def C_And(file_name):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D&M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Or(file_name):
    Instr = []
    Instr.extend(Pop("gpr", 0, file_name))
    Instr.extend(Pop("gpr", 1, file_name))
    Instr.append("@R14")
    Instr.append("D=M")
    Instr.append("@R13")
    Instr.append("M=D|M")
    Instr.extend(Push("gpr", 0, file_name))

    return Instr

def C_Not(file_name):
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
    Instr.extend(C_Sub(file_name))

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
        case "temp":
            base = 5
    return base

#   Chapter 8

def if_goto(segment, file_name):
    instr = []
    instr.extend(Pop('gpr', 0, file_name))
    instr.append("@R13")
    instr.append("D=M")
    instr.append("@" + segment)
    instr.append("D;JNE")

    return instr

def fucntion_gen(name, arguments):
    instr = []
    instr.append("(" + name + ")")
    arguments = int(arguments)

    for i in range(arguments):
        instr.extend(Push("constant", 0, ''))

    return instr

def return_gen():   # Based on figure 8.5
    instr = []
    # Frame  = LCL
    instr.append('@LCL')
    instr.append('D=M')
    instr.append("@SP")
    instr.append("A=M")
    instr.append("M=D")
    instr.append("@SP")
    instr.append("M=M+1")
    instr.extend(Pop('gpr', 2, ''))

    # RET = *(FRAME - 5(
    instr.append('@R15')
    instr.append('D=M')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('A=D')
    instr.append('D=M')
    instr.append('@R14')
    instr.append('M=D')

    # *ARG = pop()

    # Custom pop because we use too many registers
    # Go to SP-1 and store value at *SP-1 into D
    instr.append('@SP')
    instr.append('M=M-1')
    instr.append('A=M')
    instr.append('D=M')
    # Want to store the return value into *ARG
    instr.append('@ARG')
    instr.append('A=M')
    instr.append('M=D')

    # SP = ARG + 1
    instr.append('@ARG')
    instr.append('D=M')
    instr.append('D=D+1')
    instr.append('@SP')
    instr.append('M=D')

    # THAT = *(FRAME - 1)
    instr.append('@R15')
    instr.append('D=M')
    instr.append('D=D-1')
    instr.append('A=D')
    instr.append('D=M')
    instr.append('@THAT')
    instr.append('M=D')
    
    # THIS = *(FRAME - 2)
    instr.append('@R15')
    instr.append('D=M')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('A=D')
    instr.append('D=M')
    instr.append('@THIS')
    instr.append('M=D')
    
    # ARG = *(FRAME - 3)
    instr.append('@R15')
    instr.append('D=M')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('A=D')
    instr.append('D=M')
    instr.append('@ARG')
    instr.append('M=D')
    
    # LCL = *(FRAME - 4)
    instr.append('@R15')
    instr.append('D=M')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('D=D-1')
    instr.append('A=D')
    instr.append('D=M')
    instr.append('@LCL')
    instr.append('M=D')
    
    # goto RET
    instr.append('@R14')
    instr.append('A=M')
    instr.append('0;JMP')

    return instr

def call_gen (name, arg, call_count):
    instr = []
    return_label = name + ".$" + str(call_count)

    # Push return address
    instr.extend(Push("constant", return_label, ''))
    # push LCL
    instr.append('@LCL')
    instr.append('D=M')
    instr.append('@SP')
    instr.append("A=M")
    instr.append("M=D")
    instr.append("@SP")
    instr.append("M=M+1")

    # push ARG
    instr.append('@ARG')
    instr.append('D=M')
    instr.append('@SP')
    instr.append("A=M")
    instr.append("M=D")
    instr.append("@SP")
    instr.append("M=M+1")

   # push THIS
    instr.append('@THIS')
    instr.append('D=M')
    instr.append('@SP')
    instr.append("A=M")
    instr.append("M=D")
    instr.append("@SP")
    instr.append("M=M+1")

    # push THAT
    instr.append('@THAT')
    instr.append('D=M')
    instr.append('@SP')
    instr.append("A=M")
    instr.append("M=D")
    instr.append("@SP")
    instr.append("M=M+1")

    # ARG = SP - n -5
    instr.append("@SP")
    instr.append("D=M")
    instr.append("D=D-1")
    instr.append("D=D-1")
    instr.append("D=D-1")
    instr.append("D=D-1")
    instr.append("D=D-1")

    for i in range(int(arg)):
        instr.append("D=D-1")

    instr.append("@ARG")
    instr.append("M=D")

    # LCL = SP
    instr.append("@SP")
    instr.append("D=M")
    instr.append("@LCL")
    instr.append("M=D")
    
    # go to f
    instr.append(("@" + name))
    instr.append("0;JMP")

    # (return address)
    instr.append("(" + return_label + ")")

    return instr

    


