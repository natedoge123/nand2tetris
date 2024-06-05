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
                    break
                temp_token_count += 1

        elif token.text in ['static', 'field']:
            sub_routine = ET.SubElement(new_xml_tree, 'classVarDec')
            for elem in xml:

                if (temp_token_count >= token_count and temp_token_count > end_prev_parent):
                    temp = ET.SubElement(sub_routine, elem.tag)
                    temp.text = elem.text

                if elem.text == ";" and temp_token_count >= token_count:
                    end_prev_parent = temp_token_count
                    break

                temp_token_count += 1

        elif token.text in ['constructor', 'function', 'method']:
            sub_routine = ET.SubElement(new_xml_tree, 'subroutineDec')

            for elem in xml:
                temp_token_count += 1
                cond1 = temp_token_count > end_prev_parent
                cond2 = temp_token_count > token_count

                if (cond1 and cond2):
                    temp = ET.SubElement(sub_routine, elem.tag)
                    temp.text = elem.text

                if (elem.text == "(" and cond1 and cond2):
                    end_prev_parent = temp_token_count
                    break

            temp_token_count = 0
            parameter_list = ET.SubElement(sub_routine, 'parameterList')

            for elem in xml:
                temp_token_count += 1
                cond1 = temp_token_count > end_prev_parent
                cond2 = temp_token_count > token_count

                if (elem.text == ')' and cond1 and cond2):
                    end_prev_parent = temp_token_count + 1
                    temp = ET.SubElement(sub_routine, elem.tag)
                    temp.text = elem.text
                    temp_token_count = 0
                    break

                if (temp_token_count > end_prev_parent):
                    temp = ET.SubElement(parameter_list, elem.tag)
                    temp.text = elem.text

            subroutine_body = ET.SubElement(sub_routine, 'subroutineBody')

            for elem in xml:
                temp_token_count += 1
                cond1 = temp_token_count > end_prev_parent
                cond2 = temp_token_count > token_count

                if (elem.text == "}" and cond1 and cond2):
                    end_prev_parent = temp_token_count + 1
                    temp = ET.SubElement(subroutine_body, elem.tag)
                    temp.text = elem.text
                    temp_token_count = 0
                    break

                if (temp_token_count >= end_prev_parent):
                    temp = ET.SubElement(subroutine_body, elem.tag)
                    temp.text = elem.text


            for elem in xml:
                temp_token_count += 1

                if elem.text in ['let', 'if', 'else',
                                 'while', 'do', 'return']:
                    sub_statements = ET.SubElement(subroutine_body,
                                                   "statement")

                    if elem.text == 'let':
                        let_statement = ET.SubElement(sub_statements, "letStatement")
                        temp_statement_count = 0
                        cond1 = temp_token_count >= end_prev_parent

                        for item in xml:
                            temp_statement_count += 1
                            if (cond1):
                                temp = ET.SubElement(let_statement, item.tag)
                                temp.text = item.text

                            if (item.text == ";" and cond1):
                                temp = ET.SubElement(let_statement, item.tag)
                                temp.text = item.text
                                end_prev_parent = temp_token_count + 1
                                temp_token_count = 0
                                break

                    elif elem.text == 'if':
                        if_statment = ET.SubElement(sub_statements, "ifStatement")
                        cond1 = temp_token_count >= end_prev_parent

                    elif elem.text == 'while':
                        while_statement = ET.SubElement(sub_statements, "whileStatement")
                        cond1 = temp_token_count >= end_prev_parent

                    elif elem.text == 'do':
                        do_statement = ET.SubElement(sub_statements, "doStatement")
                        cond1 = temp_token_count >= end_prev_parent

                    elif elem.text == 'return':
                        return_statement = ET.SubElement(sub_statements, "returnStatement")
                        cond1 = temp_token_count >= end_prev_parent

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

