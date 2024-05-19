import files
import compliation
import myToken

import sys
from pathlib import Path


file_list = files.open_dir(sys.argv[1])

for file in file_list:
    file_string = files.read_files(file)
    tokenized = (myToken.tokenizer(file_string))
    print(tokenized)
    xmled = myToken.xmlToken(tokenized)


    files.write_file(str(xmled), sys.argv[1]+ 'TT', 'xml')





