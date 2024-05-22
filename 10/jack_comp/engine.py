import xml.etree.ElementTree as ET
from xml.dom import minidom

def runEngine(xml): #takes tokenized xml tree and gives foramtted one
    new_xml_tree = ET.Element('class')
    programStructure(xml)


    return new_xml_tree

def programStructure(xml):
    program_struct_counts = programStructureCounter(xml)

    return program_struct_counts

def programStructureCounter(xml):
    static_list = []
    field_list = []

    for elem in xml:
        if (elem.text == 'static'):
            static_list.append(elem.text)

        if (elem.text == 'field'):
            field_list.append(elem.text)
    
    print ([static_list, field_list])
    return ([static_list, field_list])


def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="    ")


