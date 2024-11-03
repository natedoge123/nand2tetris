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

        if (para_active and item.text == ')' and last_para_count == 1):
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
            temp_xml.append(statement_finder(body_list))
            continue

        if not(para_active or body_active):
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text

    return temp_xml

def subStatement_maker(xml):
    count = 0

    for item in xml:
        count += 1

    if count == 0:
        return ET.Element('statements')

    statement = statement_finder(xml)

    return statement[0]



def statement_finder(xml): 
    sub_body = ET.Element('subroutineBody')
    temp_state = ET.Element('temp')
    statements = []
    loop_words = ['let', 'if', 'else', 'while', 'do', 'return', 'var']

    let_active = False
    if_active = False
    else_active = False
    while_active = False
    do_active = False
    return_active = False
    var_active = False

    brace_count = 0
    last_brace_count = brace_count

    max_count = 0
    running_count = 0
    if_count = 0

    for item in xml:
        max_count += 1

    for item in xml:
        running_count += 1

        any_active = let_active or if_active or else_active or while_active or do_active or return_active or var_active
        
        last_brace_count = brace_count

        if item.text == '{': brace_count += 1
        if item.text == '}': brace_count -= 1

        if (item.text in loop_words and not any_active):
            match item.text:
                case 'let':
                    let_active = True
                    temp_state = ET.Element('let')

                case 'if':
                    if_active = True
                    temp_state = ET.Element('if')

                case 'while':
                    while_active = True
                    temp_state = ET.Element('while')

                case 'do':
                    do_active = True
                    temp_state = ET.Element('do')

                case 'return':
                    return_active = True
                    temp_state = ET.Element('return')

                case 'var':
                    var_active = True
                    temp_state = ET.Element('var')


        if (max_count == running_count):
            sub_body.append(statementMaker(statements))

        if (not(any_active) and not(item.text in loop_words)):
            temp = ET.SubElement(sub_body, item.tag)
            temp.text = item.text
                
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
            if (item.text == '}'):
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text

                for if_item in xml:
                    if_count += 1

                    if (if_count) == (running_count + 1):
                        if if_item.text == 'else':
                            else_active = True
                            if_active = False
                            continue
                statements.append(temp_state)
                continue

            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text

        if else_active:
            if (item.text == '}'):
                else_active = False
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                statements.append(temp_state)
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
                continue
            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text

        if var_active:
            if item.text == ';':
                var_active = False
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                var_state_xml = temp_state
                sub_body.append(statementEngine.var_state(var_state_xml))
                continue
            else:
                temp = ET.SubElement(temp_state, item.tag)
                temp.text = item.text
                
    return sub_body

def statementMaker(statements):
    state_xml = ET.Element('statements')

    # remove duplicates that occur when there is if-else statement
    no_dupe = remove_dup_keep_order(statements)

    for xml in no_dupe:
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
                print('not a statement')

    return state_xml

def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="  ")

def remove_dup_keep_order(items):
    return list(dict.fromkeys(items))


