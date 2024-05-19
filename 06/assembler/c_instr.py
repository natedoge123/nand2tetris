def read(line):
    c_inst = "111"

    if(True):
        c_inst += comp(line)

    if ("=" in line):
        c_inst += dest(line)
    else:
        c_inst += "000"

    if (";" in line):
        c_inst += jump(line)
    else:
        c_inst += "000"

    return c_inst


def comp(line):
    if (("=" in line) and (";" in line)):
        temp = line.split("=")[1]
        comp = temp.split(";")[0]

    elif ("=" in line):
        comp = line.split("=")[1]
    elif (";" in line):
        comp = line.split(";")[0]
    else:
        print("its broke")

    comp_inst = ""
    if ("M" in comp):
        comp_inst = "1"
        if (comp == "M"):
            comp_inst += "110000"
        elif(comp == "!M"):
            comp_inst += "110001"
        elif(comp == "-M"):
            comp_inst += "110011"
        elif(comp == "M+1"):
            comp_inst += "110111"
        elif(comp == "M-1"):
            comp_inst += "110010"
        elif(comp == "D+M"):
            comp_inst += "000010"
        elif(comp == "D-M"):
            comp_inst += "010011"
        elif(comp == "M-D"):
            comp_inst += "000111"
        elif(comp == "D&M"):
            comp_inst += "000000"
        elif(comp == "D|M"):
            comp_inst += "010101"

    else:
        comp_inst = "0"
        if (comp == "0"):
            comp_inst += "101010"
        elif(comp == "1"):
            comp_inst += "111111"
        elif(comp == "-1"):
            comp_inst += "111010"
        elif(comp == "D"):
            comp_inst += "001100"
        elif(comp == "A"):
            comp_inst += "110000"
        elif(comp == "!D"):
            comp_inst += "001101"
        elif(comp == "!A"):
            comp_inst += "110001"
        elif(comp == "-D"):
            comp_inst += "001111"
        elif(comp == "-A"):
            comp_inst += "110011"
        elif(comp == "D+1"):
            comp_inst += "011111"
        elif(comp == "A+1"):
            comp_inst += "110111"
        elif(comp == "D-1"):
            comp_inst += "001110"
        elif(comp == "A-1"):
            comp_inst += "110010"
        elif(comp == "D+A"):
            comp_inst += "000010"
        elif(comp == "D-A"):
            comp_inst += "010011"
        elif(comp == "A-D"):
            comp_inst += "000111"
        elif(comp == "D&A"):
            comp_inst += "000000"
        elif(comp == "D|A"):
            comp_inst += "010101"

    return comp_inst


def dest(line):
    dest_instr = '' 
    Compare_String = line.split("=")[0]
    if ("A" in Compare_String):
        dest_instr += "1"
    else:
        dest_instr += "0"
    if ("D" in Compare_String):
        dest_instr += "1"
    else:
        dest_instr += "0"
    if ("M" in Compare_String):
        dest_instr += "1"
    else:
        dest_instr += "0"

    return dest_instr



def jump(line):
    Print_Line = ""
    Check = line[-3:]

    if (Check == "JGT"):
        Print_Line += "001"
    elif(Check == "JEQ"):
        Print_Line += "010"
    elif(Check == "JGE"):
        Print_Line += "011"
    elif(Check == "JLT"):
        Print_Line += "100"
    elif(Check == "JNE"):
        Print_Line += "101"
    elif(Check == "JLE"):
        Print_Line += "110"
    elif(Check == "JMP"):
        Print_Line += "111"
    else:
        Print_Line += "000"

    return(Print_Line)


