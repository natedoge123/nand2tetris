import files
import myToken
import engine

import sys


file_list = files.open_dir(sys.argv[1])

for file in file_list:
    #   Getting the file name right
    file_name = str(file).split('/')[-1]
    file_name = file_name.split('.')[0]
    #print(file_name)

    #   Tokenize file 
    file_string = files.read_files(file)
    tokenized = (myToken.tokenizer(file_string))
    #print(tokenized)
    xmled = myToken.xmlToken(tokenized)
    print(myToken.xmlPrint(xmled))

    #   Format the tokenized xml to the correcto output
    formatted_xml = engine.run(xmled)
    print(formatted_xml)


    #   Save the files
    write_name = sys.argv[1] + "/" + file_name + "TT"
    files.write_file(str(xmled), write_name, 'xml')


