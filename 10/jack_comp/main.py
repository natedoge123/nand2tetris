import files
import myToken
import engine
import enginetwo
import enginethree

import sys


file_list = files.open_dir(sys.argv[1])

for file in file_list:
    #   Getting the file name right
    file_name = str(file).split('/')[-1]
    file_name = file_name.split('.')[0]
    #print(file_name)

    #   Tokenize file 
    file_string = files.read_files(file)
    #print(file_string)
    tokenized = (myToken.tokenizer(file_string))
    #print(tokenized)
    xmled = myToken.xmlToken(tokenized)

    #   Format the tokenized xml to the correcto output
    #formatted_xml = engine.run(xmled)
    formatted_xml = enginetwo.classMaker(xmled)
    #formatted_xml = enginethree.CompileClass(xmled)
    #print(myToken.xmlPrint(formatted_xml_2))
    #print(formatted_xml)


    #   Save the files
    write_name = sys.argv[1] + "/" + file_name + "Token"
    files.write_file(myToken.xmlPrint(xmled), write_name, 'xml')

    write_name = sys.argv[1] + "/" + file_name + "Class"
    files.write_file(myToken.xmlPrint(formatted_xml), write_name, 'xml')
