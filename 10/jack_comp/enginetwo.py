from re import sub
import xml.etree.ElementTree as ET
from xml.dom import minidom

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


    #print(xmlPrint(class_tree))
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
    temp_xml = ET.Element('subroutineDec')
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
    print(xmlPrint(xml))
    temp_xml = ET.Element('subroutineDec')
    para_list = ET.Element('parameterList')
    subroutine_body = ET.Element('subroutine_body')

    para_count = 0
    last_para_count = para_count

    para_list_done = False
    

    for item in xml:
        last_para_count = para_count

        if item.text == '(':
            para_count += 1
        if item.text == ')':
            para_count -= 1

        if (para_count == 0 and last_para_count == 0 and para_list_done = False):
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text


        if (para_count == 0 and last_para_count == 0):
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text

        elif (para_count == 0 and last_para_count == 1):
            temp = ET.SubElement(temp_xml, item.tag)
            temp.text = item.text
            


    return temp_xml

def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="  ")

