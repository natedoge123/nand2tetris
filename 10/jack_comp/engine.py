import xml.etree.ElementTree as ET
from xml.dom import minidom

def run(xml): #takes tokenized xml tree and gives foramtted one
    new_xml_tree = ET.Element('class')
    count_para = 0
    count_braces = 0
    count_bracket = 0

    for elem in xml:

        if elem.text in ['static', 'field']:
            sub_routine = ET.SubElement(new_xml_tree, 'classVarDec')

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

            if elem.text == "(": count_para += 1
            if elem.text == "{": count_braces += 1
            if elem.text == "[": count_para += 1

            if elem.text == ")": count_para -= 1
            if elem.text == "}": count_braces -= 1
            if elem.text == "]": count_para -= 1

            print('cringe')

    return xmlPrint(new_xml_tree)


def addParentToTag(root, tag, new_parent):
    elem_to_move = root.findall(tag)

    if not elem_to_move:
        return
    
    new_parent = ET.Element(new_parent)

    root.append(new_parent)

    for elem in elem_to_move:
        root.remote(elem)



def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="    ")

