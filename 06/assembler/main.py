import os
import time
import sys

import a_instr
import c_instr
import l_instr
import read
import write
import symbols


File_Read = read.load_file(sys.argv[1])

Symbol_Table = symbols.constructor()
symbols.runs(File_Read, Symbol_Table);

Start_Time = time.time()

Binary_List = []
Address = 16

for line in File_Read:
    Command = read.command_type(line)

    if (Command == "A"):
        if (line[1].isdigit()):
            Binary_List.append(a_instr.read(line))
        else:
            Symbol = line[1:]
            if Symbol not in Symbol_Table:
                Symbol_Table[Symbol] = Address
                Address += 1
            New_Line = "@" + str(Symbol_Table[Symbol])
            Binary_List.append(a_instr.read(New_Line))

    elif(Command == "L"):
        word = False
        #Binary_List.append(l_instr.read(line))
    else:
        Binary_List.append(c_instr.read(line))
    #print(Binary_List[-1])

name = sys.argv[2]
write.write(Binary_List, name)


print("Done. Run Time %s seconds" % (time.time() - Start_Time))
