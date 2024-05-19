def runs(data, table):

    Address = 0

    for line in data:
        if (line[0] == "("):
            Symbol = line[1:-1]
            table[Symbol] = Address
        else:
            Address += 1



def constructor():

    Table = {
        "SP":"0",
        "LCL":"1",
        "ARG":"2",
        "THIS":"3",
        "THAT":"4",
        "R0":"0",
        "R1":"1",
        "R2":"2",
        "R3":"3",
        "R4":"4",
        "R5":"5",
        "R6":"6",
        "R7":"7",
        "R8":"8",
        "R9":"9",
        "R10":"10",
        "R11":"11",
        "R12":"12",
        "R13":"13",
        "R14":"14",
        "R15":"15",
        "SCREEN":"16384",
        "KBD":"24576"
    }

    return Table

