from re import sub
#from sys import last_traceback
import xml.etree.ElementTree as ET
from xml.dom import minidom
import statementEngine

def classMaker(xml):
    class_tree = ET.Element('class')
    temp_tree = ET.Element('temp')
    brace_count = 0
    last_brace_count = brace_count

    for item in xml:
        last_brace_count = brace_count

        if (item.text == '{'):
            brace_count += 1
        if (item.text == '}'):
            brace_count -= 1

        if (brace_count == 0 and last_brace_count == 0):
            temp = ET.SubElement(class_tree, item.tag)
            temp.text = item.text

        elif (brace_count == 0 and last_brace_count == 1):
            class_var_dec_list = classVarDecFinder(temp_tree)
            subroutine_dec_list = subrountineFinder(temp_tree)

            for xml_tree in class_var_dec_list:
                class_tree.append(xml_tree)

            for xml_tree in subroutine_dec_list:
                class_tree.append(xml_tree)

            temp = ET.SubElement(class_tree, item.tag)
            temp.text = item.text

        elif (brace_count != 0 and last_brace_count !=0):
            temp = ET.SubElement(temp_tree, item.tag)
            temp.text = item.text

        elif (brace_count == 1 and last_brace_count == 0):
            temp = ET.SubElement(class_tree, item.tag)
            temp.text = item.text

    return class_tree

def classVarDecFinder(xml):
    xml_list = []
    temp_xml = ET.Element('temp')

    var_dec_active = False
    brace_count = 0

    for item in xml:

        if item.text == '{':
            brace_count += 1
        if item.text == '}':
            brace_count -= 1

        if item.text in ['static', 'field']:
            temp_xml = ET.Element('classVarDec')
            var_dec_active = True

        if var_dec_active:
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text

        if item.text == ';' and var_dec_active:
            xml_list.append(temp_xml)
            var_dec_active = False

    return xml_list

def subrountineFinder(xml):
    xml_list = []
    temp_xml = ET.Element('temp')
    sub_active = False

    brace_count = 0

    for item in xml:
        last_brace_count = brace_count

        if item.text in ['constructor', 'function', 'method']:
            temp_xml = ET.Element('temp')
            brace_count = 0
            last_brace_count = brace_count
            sub_active = True

        if item.text == '{':
            brace_count += 1
        if item.text == '}':
            brace_count -= 1

        if (sub_active):
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text
            
        if ((brace_count == 0) and (last_brace_count == 1)):
            xml_list.append(subroutineDecBuilder(temp_xml))
            sub_active = False

    return xml_list

def subroutineDecBuilder(xml):
    temp_xml = ET.Element('subroutineDec')
    para_list = ET.Element('parameterList')
    body_list = ET.Element('body_list')

    para_count = 0
    para_done = False
    para_active = False

    brace_count = 0
    body_done = False
    body_active = False


    for item in xml:

        last_para_count = para_count
        last_brace_count = brace_count

        if item.text == '(': para_count += 1
        if item.text == ')': para_count -= 1

        if item.text == '{': brace_count += 1
        if item.text == '}': brace_count -= 1

        if (not para_done and item.text == '('):
            para_active = True
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text
            continue
            
        if (para_active and item.text != ')'):
            temp = ET.SubElement(para_list, item.tag)
            temp.text = item.text
            continue

        if (para_active and item.text == ')'):
            temp_xml.append(para_list)
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text
            para_active = False
            para_done = True
            continue

        if (not body_done and item.text == '{'):
            body_active = True
            temp = ET.SubElement(body_list, item.tag)
            temp.text = item.text
            continue

        if (body_active and brace_count > 0):
            temp = ET.SubElement(body_list, item.tag)
            temp.text = item.text
            continue

        if (body_active and brace_count == 0 and last_brace_count == 1):
            temp = ET.SubElement(body_list, item.tag)
            temp.text = item.text
            temp_xml.append(subroutineBody(body_list))
            continue

        if not(para_active or body_active):
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text

    return temp_xml

def subroutineBody(xml):
    sub_body = ET.Element('subroutineBody')
    temp_state = ET.Element('temp')
    statements = []
    loop_words = ['let', 'if', 'else', 'while', 'do', 'return']

    let_active = False
    if_active = False
    while_active = False
    do_active = False
    return_active = False

    brace_count = 0
    last_brace_count = brace_count

    for item in xml:
        any_active = let_active or if_active or while_active or do_active or return_active
        
        last_brace_count = brace_count

        if item.text == '}': brace_count += 1
        if item.text == '{': brace_count -= 1

        if (item.text in loop_words and not any_active):
            match item.text:
                case 'let':
                    let_active = True
                    temp_state = ET.Element('let')

                case 'if':
                    if_active = True
                    temp_state = ET.Element('if')

                case 'else':
                    if_active = True

                case 'while':
                    while_active = True
                    temp_state = ET.Element('while')

                case 'do':
                    do_active = True
                    temp_state = ET.Element('do')

                case 'return':
                    return_active = True
                    temp_state = ET.Element('return')

        if let_active:
            if item.text == ';':
                let_active = False
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                statements.append(temp_state)
                continue
            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                
        if if_active:
            if (brace_count == 0 and item.text == '}'):
                if_active = False
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                statements.append(temp_state)
                sub_body.append(statementMaker(statements))
                continue
            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text

        if while_active:
            if (brace_count == 0 and last_brace_count == 1):
                while_active = False
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                statements.append(temp_state)
                sub_body.append(statementMaker(statements))
                continue
            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text

        if do_active:
            if item.text == ';':
                do_active = False
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                statements.append(temp_state)
                sub_body.append(statementMaker(statements))
                continue
            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text

        if return_active:
            if item.text == ';':
                return_active = False
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                statements.append(temp_state)
                sub_body.append(statementMaker(statements))
                continue
            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text

        if (not(any_active) and not(item.text in loop_words)):
                temp = ET.SubElement(sub_body, item.tag)
                temp.text = item.text

    return sub_body

def statementMaker(statements):
    state_xml = ET.Element('statements')

    for xml in statements:
        check = xml[0].text
        
        match check:
            case 'let':
                state_xml.append(statementEngine.let_state(xml))
            case 'if':
                state_xml.append(statementEngine.if_state(xml))
            case 'while':
                state_xml.append(statementEngine.while_state(xml))
            case 'do':
                state_xml.append(statementEngine.do_state(xml))
            case 'return':
                state_xml.append(statementEngine.return_state(xml))
            case _:
                print('errrrror')

    return state_xml


def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="  ")

