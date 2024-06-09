from types import new_class
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

                if elem.text in ['let', 'if', 'else',
                                 'while', 'do', 'return']:
                    sub_statements = ET.SubElement(subroutine_body,
                                                   "statement")

                    if elem.text == 'let':
                        let_statement = ET.SubElement(sub_statements, "letStatement")
                        temp_statement_count = 0

                        for item in xml:
                            temp_statement_count += 1
                            cond1 = temp_token_count >= end_prev_parent

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
                        temp_statement_count = 0

                        for item in xml:
                            temp_token_count += 1
                            cond1 = temp_token_count >= end_prev_parent

                            if (cond1):
                                temp = ET.SubElement(if_statment, item.tag)
                                temp.text = item.text

                            if (cond1 and item.text == "}"):
                                break

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

def run2(xml):
    new_xml_tree = ET.Element("class")
    main_count = 0
    end_prev_parent = 0

    for token in xml:
        count_1 = 0
        
        if token.text in ['class']:
            for elem in xml:
                #   Main cond to check if in right part of loop
                cond_0 = (count_1 >= main_count) and (count_1 >= end_prev_parent)

                if (cond_0):
                    temp = ET.SubElement(new_xml_tree, elem.tag)
                    temp.text = elem.text

                if (cond_0 and elem.text == "{"):
                    end_prev_parent = count_1 + 1
                    break

                count_1 += 1
        elif token.text in ['static', 'field']:
            sub_routine = ET.SubElement(new_xml_tree, "classVarDec")
            count_1 = 0

            for elem in xml:
                #   Main cond to check if in right part of loop
                cond_0 = (count_1 >= main_count) and (count_1 >= end_prev_parent)

                if (cond_0):
                    temp = ET.SubElement(sub_routine, elem.tag)
                    temp.text = elem.text

                if (cond_0 and elem.text == ";"):
                    end_prev_parent = count_1 + 1 
                    break

                count_1 += 1

        elif token.text in ['constructor', 'function', 'method']:
            #sub_routine = ET.SubElement(new_xml_tree, 'subroutineDec')
            temp_tree = ET.Element('subroutineDec')
            #   Main cond to check if in right part of loop
            count_1 = 0
            count_braces = 0
            last_count_braces = count_braces

            for elem in xml:
                cond_0 = (count_1 >= main_count) and (count_1 >= end_prev_parent)

                if (cond_0):

                    if (elem.text == "{"):
                        count_braces += 1
                    if (elem.text == "}"):
                        count_braces -= 1

                    temp = ET.SubElement(temp_tree, elem.tag)
                    temp.text = elem.text

                    if ((count_braces == 0) and (last_count_braces > count_braces)):
                        print(xmlPrint(temp_tree))
                        sub = subroutine_maker(temp_tree)
                        end_prev_parent = count_1 + 1
                        break
                    last_count_braces = count_braces
                count_1 += 1

    return new_xml_tree

def subroutine_maker(xml):
    sub_tree = ET.Element('subroutineDec')
    token_count = 0

    for token in xml:
        token_count += 1

        if ():

    return sub_tree

def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="    ")






