import xml.etree.ElementTree as ET
from xml.dom import minidom

def classMaker(xml):
    class_tree = ET.Element("class")
    temp_tree = ET.Element('temp')
    brace_count = 0
    last_brace_count = brace_count

    for item in xml:
        last_brace_count = brace_count

        if (item.text == '{'):
            brace_count += 1
        if (item.text == '}'):
            brace_count -= 1

        print(brace_count)

        if (brace_count == 0 and last_brace_count == 0):
            temp = ET.SubElement(class_tree, item.tag)
            temp.text = item.text

        elif(brace_count == 0 and last_brace_count == 1):
            class_tree.append(classVarDec(temp_tree))
            class_tree.append(subroutineDec(temp_tree))

            temp = ET.SubElement(class_tree, item.tag)
            temp.text = item.text

        elif (brace_count != 0):
            temp = ET.SubElement(temp_tree, item.tag)
            temp.text = item.text


    print(xmlPrint(class_tree))
    return class_tree

def classVarDec(xml):
    class_var_dec = ET.Element('classVarDec')
    var_dec_active = False

    for item in xml:
        if item.text in ['static', 'field']:
            var_dec_active = True

        if var_dec_active:
            temp = ET.SubElement(class_var_dec, item.tag)
            temp.text = item.text

        if item.text == ';':
            var_dec_active = False

    return class_var_dec

def subrountineFinder(xml):
    subroutine_dec = ET.Element('subroutineDec')
    sub_active = False

    for item in xml:
        if item.text in ['constructor', 'function', 'method']:
            sub_active = True
            brace_count = 0
            last_brace_count = brace_count

        if sub_active:
            temp = ET.SubElement(subroutine_dec, item.tag)
            temp.text = item.text

    return subroutine_dec

def subroutineDec(xml):
    temp = ET.Element('temp')

    return temp



def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="  ")

