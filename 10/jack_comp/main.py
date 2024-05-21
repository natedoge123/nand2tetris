import files
import compliation
import myToken

import sys
from pathlib import Path


file_list = files.open_dir(sys.argv[1])

for file in file_list:
    file_name = str(file).split('/')[-1]
    file_name = file_name.split('.')[0]
    print(file_name)
    file_string = files.read_files(file)
    tokenized = (myToken.tokenizer(file_string))
    #print(tokenized)
    xmled = myToken.xmlToken(tokenized)

    write_name = sys.argv[1] + "/" +file_name + "TT"
    print(write_name)

    files.write_file(str(xmled), write_name, 'xml')


