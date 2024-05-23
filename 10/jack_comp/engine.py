import xml.etree.ElementTree as ET
from xml.dom import minidom

def run(xml): #takes tokenized xml tree and gives foramtted one
    new_xml_tree = ET.Element('class')

    for i, elem in enumerate(xml):

        if elem.tag == 'keyword' and elem.text == 'class':
            temp = ET.SubElement(new_xml_tree, elem.tag)
            temp.text = elem.text
            
            temp1 = ET.SubElement(new_xml_tree, elem[i+1].tag)
            temp1.text = elem.text



    return new_xml_tree


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

