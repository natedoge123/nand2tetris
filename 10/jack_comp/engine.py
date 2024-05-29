import xml.etree.ElementTree as ET
from xml.dom import minidom

def run(xml): #takes tokenized xml tree and gives foramtted one
    new_xml_tree = ET.Element('class')
    counters = [0,0,0,0] # ( { [ ;

    for elem in xml:

        if elem.text in ['static', 'field']:
            print("static or field")
            sub_routine = ET.SubElement(new_xml_tree, 'classVarDec')
            for elem in xml:

                temp = ET.SubElement(sub_routine, elem.tag)
                temp.text = elem.text
                print(ET.tostring(temp))

                if elem.text == ";":
                    counters[3] += 1
                    break

        elif elem.text in ['constructor', 'function', 'method']:
            sub_routine = ET.SubElement(new_xml_tree, 'subroutineDec')
            parameter_list = ET.SubElement(sub_routine, 'parameterList')
            subroutine_body = ET.SubElement(sub_routine, 'subroutineBody')
            var_dec = ET.SubElement(sub_routine, 'varDec')

        elif elem.text in ['let', 'if', 'else', 'while', 'do', 'return']:

            if elem.text == 'let':
                print(elem.text)

            elif elem.text == 'if':
                print(elem.text)

            elif elem.text == 'else':
                print(elem.text)

            elif elem.text == 'while':
                print(elem.text)

            elif elem.text == 'do':
                print(elem.text)

            elif elem.text == 'return':
                print(elem.text)

        elif elem.tag in ['integerConstant', 'stringConstant', 'keywordConstant']:
            print(elem.text)

        else:

            print(counters)

    return xmlPrint(new_xml_tree)

def addParentToTag(root, tag, new_parent):
    elem_to_move = root.findall(tag)

    if not elem_to_move:
        return
    
    new_parent = ET.Element(new_parent)

    root.append(new_parent)

    for elem in elem_to_move:
        root.remote(elem)


def symbolCount(counter, symbol):

    if symbol == "(": counter[0] += 1
    if symbol == "{": counter[1] += 1
    if symbol == "[": counter[2] += 1
    if symbol == ";": counter[3] += 1

    if symbol == ")": counter[0] -= 1
    if symbol == "}": counter[1] -= 1
    if symbol == "]": counter[2] -= 1

    return counter
    
def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="    ")

