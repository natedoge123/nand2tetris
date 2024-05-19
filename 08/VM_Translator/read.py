import glob
import os

def open_dir(dir_path):
    files = glob.glob(os.path.join(dir_path, f'*.vm'))
    lines = []
    for file_path in files:
        lines.append('~' + os.path.basename(file_path))
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    if not line.startswith('/'):
                        lines.append(line.strip())

    return lines


def comment_strip(data_in):
    temp = []
    data_out = []
    for line in data_in:
        if line.strip():

            if not(line[0] == "/"):
                temp.append(line.strip())
    for item in temp:
        data_out.append(item.split('/')[0])
        
    return data_out

def write(Hack_List, file_path):
    File_Name = file_path + ".asm"
    with open(File_Name, "w") as file:
        for line in Hack_List:
            file.write(f"{line}\n")

