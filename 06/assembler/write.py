
def write(Binary_List, name):
    File_Name = name + '.hack'
    with open(File_Name, "w") as file:
        for line in Binary_List:
            file.write(f"{line}\n")
