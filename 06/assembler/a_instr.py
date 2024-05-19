def read(line):
    Temp_Int = to_int(line[1:])
    Bin_Int = bin(Temp_Int[1])[2:]
    Bin_Int_Padded = Bin_Int.zfill(16)

    return Bin_Int_Padded


def to_int(s):
    try:
        return (True, int(s))
    except ValueError:
        return (False, False)
