from types import new_class
import xml.etree.ElementTree as ET
from xml.dom import minidom

def run(xml):
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
                        #print(xmlPrint(temp_tree))
                        sub = subroutine_maker(temp_tree)
                        #print(xmlPrint(sub))
                        end_prev_parent = count_1 + 1
                        break
                    last_count_braces = count_braces
                count_1 += 1
            new_xml_tree.append(sub)


    return new_xml_tree

def subroutine_maker(xml):
    sub_tree = ET.Element('subroutineDec')
    token_count = 0
    para_list_done = False
    body_list_done = False
    end_prev_parent = 0

    for token in xml:

        if (token.text == "(" and not para_list_done):  #Parameter List
            temp_count = 0

            for item in xml:
                temp_count += 1
                cond_0 = (temp_count > token_count) and (temp_count > end_prev_parent)

                if cond_0:

                    if (item.text == "("):
                        temp = ET.SubElement(sub_tree, item.tag)
                        temp.text = item.text
                        para_list = ET.SubElement(sub_tree, "parameterList")
                        continue

                    if (item.text != ")"):
                        temp = ET.SubElement(para_list, item.tag)
                        temp.text = item.text

                    if (item.text == ")"):
                        temp = ET.SubElement(sub_tree, item.tag)
                        temp.text = item.text
                        para_list_done = True
                        end_prev_parent = token_count + 1
                        break
                else:
                    temp = ET.SubElement(sub_tree, item.tag)
                    temp.text = item.text

        if (token.text == "{" and not body_list_done):  #Parameter List
            temp_count = 0
            body_list = ET.SubElement(sub_tree, "subroutineBody")
            temp_tree = ET.Element("statement_list")
            count_braces = 0
            last_count_braces = count_braces

            for item in xml:
                cond_0 = (temp_count >= token_count) and (temp_count >= end_prev_parent)

                if cond_0:

                    if (item.text == "{"):
                        count_braces += 1
                    if (item.text == "}"):
                        count_braces -= 1

                    if ((count_braces == 1) and (last_count_braces == 0)):
                        temp = ET.SubElement(body_list, item.tag)
                        temp.text = item.text

                    elif ((count_braces == 0) and (last_count_braces == 1)):
                        dump = 2

                    else:
                        temp = ET.SubElement(temp_tree, item.tag)
                        temp.text = item.text

                    if ((count_braces == 0) and (last_count_braces > count_braces)):
                        statement = statements(temp_tree)
                        #print(xmlPrint(statement))
                        body_list.append(statement)

                    if ((count_braces == 0) and (last_count_braces == 1)):
                        temp = ET.SubElement(body_list, item.tag)
                        temp.text = item.text

                    last_count_braces = count_braces
                temp_count += 1
        token_count += 1

    sub_tree.append(body_list)

    return sub_tree

def statements(xml):
    sub_routine = ET.Element('statements')
    expression_tree = ET.Element('exp')

    counter = 0
    end_prev_parent = 0

    let_active = False
    if_active = False
    else_active = False
    while_active = False
    do_active = False
    return_active = False
    exp_active = False

    for item in xml:
        any_active = (let_active or if_active or while_active or do_active or return_active)
        counter += 1

        match item.text:
            case 'let':
                let_active = True
                state_let = ET.SubElement(sub_routine, "letStatement")
                temp = ET.SubElement(state_let, item.tag)
                temp.text = item.text
                let_expression = False
                continue

            case 'if':
                if_active = True
                state_if = ET.SubElement(sub_routine, "ifStatement")
                temp = ET.SubElement(state_if, item.tag)
                temp.text = item.text
                continue

            case 'else':
                else_active = True
                state_else = ET.SubElement(sub_routine, "else")
                temp = ET.SubElement(state_else, item.tag)
                temp.text = item.text
                continue

            case 'while':
                while_active = True
                state_while = ET.SubElement(sub_routine, "whileStatement")
                temp = ET.SubElement(state_while, item.tag)
                temp.text = item.text
                continue

            case 'do':
                do_active = True
                state_do = ET.SubElement(sub_routine, "doStatement")
                temp = ET.SubElement(state_do, item.tag)
                temp.text = item.text
                continue

            case 'return':
                return_active = True
                state_return = ET.SubElement(sub_routine, "returnStatement")
                temp = ET.SubElement(state_return, item.tag)
                temp.text = item.text
                continue
                

        if (let_active):

            if (item.text == ";"):
                let_active = False
                exp_active = False
                temp_expression = Expression(expression_tree)
                expression_tree = ET.Element('exp')
                state_let.append(temp_expression)

                temp = ET.SubElement(state_let, item.tag) #append ; to the end of the expression
                temp.text = item.text

                continue #skip rest of this cycle

            if exp_active and item.text != ';':
                temp = ET.SubElement(expression_tree, item.tag)
                temp.text = item.text

            else:
                temp = ET.SubElement(state_let, item.tag)
                temp.text = item.text

            if (item.text == '='):
                exp_active = True

        if (if_active):
            temp = ET.SubElement(expression_tree, item.tag)
            temp.text = item.text

            if (item.text == "}"):
                if_active = False

        if (else_active):
            temp = ET.SubElement(expression_tree, item.tag)
            temp.text = item.text

            if (item.text == "}"):
                if_active = False

        if (while_active):
            temp = ET.SubElement(expression_tree, item.tag)
            temp.text = item.text

            if (item.text == "}"):
                if_active = False

        if (do_active):
            temp = ET.SubElement(sub_routine, item.tag)
            temp.text = item.text

            if (item.text == ";"):
                if_active = False

        if (return_active):
            temp = ET.SubElement(state_return, item.tag)
            temp.text = item.text

            if (item.text == ";"):
                if_active = False


    return sub_routine

def Expression(xml):
    print(xmlPrint(xml))
    expression_list = ET.Element('expression')
    counter = 0
    term_active = False

    for item in xml:

        if item.tag in 'identifier':
            term_active = True
            term = ET.SubElement(expression_list, 'term')
            temp = ET.SubElement(term, item.tag)

        else:
            term_active = False

        if term_active:
            temp.text = item.text

        else:
            temp = ET.SubElement(expression_list, item.tag)
            temp.text = item.text


    print(xmlPrint(expression_list))
    return expression_list


def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="    ")




