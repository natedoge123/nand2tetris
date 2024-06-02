import xml.etree.ElementTree as ET
from xml.dom import minidom

def run(xml): #takes tokenized xml tree and gives foramtted one
    new_xml_tree = ET.Element('class')
    token_count = 0
    end_prev_parent = 0

    for token in xml:
        temp_token_count = 0

        if token.text in ['class']:
            for elem in xml:

                if (temp_token_count >= token_count):
                    temp = ET.SubElement(new_xml_tree, elem.tag)
                    temp.text = elem.text

                if (elem.text == "{"):
                    end_prev_parent = temp_token_count;
                    print(end_prev_parent)
                    break
                temp_token_count += 1

        elif token.text in ['static', 'field']:
            sub_routine = ET.SubElement(new_xml_tree, 'classVarDec')
            for elem in xml:

                if (temp_token_count >= token_count and temp_token_count > end_prev_parent):
                    temp = ET.SubElement(sub_routine, elem.tag)
                    temp.text = elem.text
                    print(ET.tostring(temp))

                if elem.text == ";" and temp_token_count >= token_count:
                    end_prev_parent = temp_token_count
                    print(end_prev_parent)
                    break
                temp_token_count += 1

        elif token.text in ['constructor', 'function', 'method']:
            sub_routine = ET.SubElement(new_xml_tree, 'subroutineDec')

            parameter_list = ET.SubElement(sub_routine, 'parameterList')
            subroutine_body = ET.SubElement(sub_routine, 'subroutineBody')
            var_dec = ET.SubElement(sub_routine, 'varDec')

            for elem in xml:

                if elem.text in ['let', 'if', 'else', 'while', 'do', 'return']:

                    if token.text == 'let':
                        print(token.text)

                    elif token.text == 'if':
                        print(token.text)

                    elif token.text == 'else':
                        print(token.text)

                    elif token.text == 'while':
                        print(token.text)

                    elif token.text == 'do':
                        print(token.text)

                    elif token.text == 'return':
                        print(token.text)

        elif token.tag in ['integerConstant', 'stringConstant', 'keywordConstant']:
            print(token.text)

        else:
            one = 1

        token_count += 1
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

