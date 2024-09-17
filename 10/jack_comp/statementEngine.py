import xml.etree.ElementTree as ET
import enginetwo

def let_state(xml):
    stt = ET.Element('letStatement')
    exp_xml = ET.Element('exp')
    exp_act = False

    for item in xml:

        if (item.text == ']' or item.text == ';'):
            exp_act = False
            stt.append(expression(exp_xml))

        if not(exp_act):
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text

        elif (exp_act):
            temp = ET.SubElement(exp_xml, item.tag)
            temp.text = item.text

        if (item.text == '[' or item.text == '='):
            exp_act = True

    return stt

def if_state(xml):
    stt = ET.Element('ifStatement')
    exp_xml = ET.Element('exp')
    state_xml = ET.Element('state')

    exp_act = False #Expresion Active
    exp_done = False
    state_act = False #Statment Active

    para_count = 0
    last_para_count = para_count

    brace_count = 0
    last_brace_count = brace_count

    for item in xml:
        last_para_count = para_count
        if (item.text == '('):  para_count += 1
        if (item.text == ')'):  para_count -= 1

        last_brace_count = brace_count
        if (item.text == '{'):  brace_count += 1
        if (item.text == '}'):  brace_count -= 1

        if ((para_count == 1 and last_para_count == 0) and not exp_done):
            exp_act = True
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text
            continue

        if ((para_count == 0 and last_para_count == 1) and not exp_done):
            exp_act = False
            exp_done = True
            stt.append(expression(exp_xml))

            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text

            continue

        if (brace_count == 1 and last_brace_count == 0):
            state_act = True
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text
            continue

        if (brace_count == 0 and last_brace_count == 1):
            state_act = False
            stt.append(enginetwo.subStatement_maker(state_xml))
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text
            continue

        if (exp_act and not exp_done):
            temp = ET.SubElement(exp_xml, item.tag)
            temp.text = item.text

        elif (exp_done and not state_act):
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text

        elif (exp_done and state_act):
            temp = ET.SubElement(state_xml, item.tag)
            temp.text = item.text

        else:
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text

    return stt

def while_state(xml):
    stt = ET.Element('whileStatement')
    exp_xml = ET.Element('exp')
    state_xml = ET.Element('state')
    
    exp_act = False
    state_act = False

    para_count = 0
    last_para_count = para_count
    brace_count = 0
    last_brace_count = brace_count

    for item in xml:
        last_para_count = para_count
        last_brace_count = brace_count

        if(item.text == '('): para_count += 1
        if(item.text == ')'): para_count -= 1
        if (para_count >= 1) and (last_para_count == 0): exp_act = True
        if (para_count == 0) and (last_para_count >= 1): exp_act = False

        if(item.text == '{'): brace_count += 1
        if(item.text == '}'): brace_count -= 1
        if (brace_count >= 1) and (last_brace_count == 0): state_act = True
        if (brace_count == 0) and (last_brace_count >= 1): state_act = False

        if (exp_act):
            temp = ET.SubElement(exp_xml, item.tag)
            temp.text = item.text

        if (state_act):
            temp = ET.SubElement(state_xml, item.tag)
            temp.text = item.text

        if (para_count == 0) and (last_para_count >= 1):
            stt.append(expression(exp_xml))

        if (brace_count == 0) and (last_brace_count >= 1):
            print('')
            #stt.append(enginetwo.statementMaker(state_xml))

    return stt

def do_state(xml):

    stt = ET.Element('doStatement')
    exp_xml = ET.Element('exp')

    exp_act = False

    para_count = 0
    last_para_count = para_count

    for item in xml:
        last_para_count = para_count

        if(item.text == '('): para_count += 1
        if(item.text == ')'): para_count -= 1
        if (para_count >= 1) and (item.text == '('): exp_act = True
        if (para_count == 0) and (item.text == ')'): exp_act = False

        if (exp_act):
            temp = ET.SubElement(exp_xml, item.tag)
            temp.text = item.text

        if (para_count == 0) and (last_para_count >= 1):
            temp = ET.SubElement(exp_xml, item.tag)
            temp.text = item.text
            stt.append(expressionList(exp_xml))

        if not(exp_act) or item.text == '(':
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text


    return stt

def return_state(xml):
    stt = ET.Element('returnStatement')
    exp_xml = ET.Element('exp')
    length_return = 0

    for item in xml:
        length_return += 1

    for item in xml:
        if not(item.text == 'return' or item.text == ';'):
            temp = ET.SubElement(exp_xml, item.tag)
            temp.text = item.text
        
        elif(item.text == ';'):
            if length_return == 2:
                temp = ET.SubElement(stt, item.tag)
                temp.text = item.text
            else:
                stt.append(expression(exp_xml))
                temp = ET.SubElement(stt, item.tag)
                temp.text = item.text

        else:
            temp = ET.SubElement(stt, item.tag)
            temp.text = item.text

    return stt

def var_state(xml):
    stt = ET.Element('varDec')

    for item in xml:
        temp = ET.SubElement(stt, item.tag)
        temp.text = item.text

    return stt

def expression(xml):
    count = 0
    for item in xml:
        count += 1

    exp = ET.Element('expression')

    for item in xml:
        if item.tag == 'identifier' or item.tag == 'keyword':
            term = ET.SubElement(exp, 'term')
            temp = ET.SubElement(term, item.tag)
            temp.text = item.text

    return exp

def expressionList(xml):
    exp_list = ET.Element('expressionList')
    exp = ET.Element('exp')
    exp_array = []
    para_count =0 

    for item in xml:

        if (item.text == '('):
            para_count += 1
        if (item.text == ')'):
            para_count -= 1

        if (item.text == ',' or item.text == ';'):
            temp = ET.SubElement(exp_list, item.tag)
            temp.text = item.text
            exp_array.append(exp)
            exp = ET.Element('exp')

        elif (para_count == 0 and item.text == ')'):
            exp_array.append(exp)
            exp = ET.Element('exp')

        if (item.text == '('):
            continue
        else:
            temp = ET.SubElement(exp, item.tag)
            temp.text = item.text

    for item in pruneExpressionList(exp_array):
        exp_list.append(item)

    return exp_list

def pruneExpressionList(exps):
    pruned = []

    for item in exps:
        print(enginetwo.xmlPrint(item))

    return pruned
