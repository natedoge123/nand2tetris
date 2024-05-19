def open_file(File_Path):
    with open(File_Path, encoding = "utf-8") as f:
        data = comment_strip(f)
    return data

def comment_strip(data_in):
    data_out = []
    for line in data_in:
        if line.strip():
            if "//" not in line:
                data_out.append(line.strip())
    return data_out

def write(Hack_List, file_path):
    File_Name = file_path + ".asm"
    with open(File_Name, "w") as file:
        for line in Hack_List:
            file.write(f"{line}\n")

def path_explode(file_path):
    file_path.split("/")
    return(file_path)
