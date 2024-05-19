import os

def load_file(file_path):
    with open(file_path, encoding = "utf-8") as f:
        data = comment_strip(f)
    return data

def comment_strip(data_in):
    data_out = []
    for line in data_in:
        if line.strip():
            if "//" not in line:
                data_out.append(line.strip())
    return data_out

def command_type(line):
    if (line[0] == "@"):
        command = "A"
    elif(line[0] == "("):
        command = "L"
    else:
        comman d= "C"

    return command
        
