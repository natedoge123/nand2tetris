import xml.etree.ElementTree as ET
import enginetwo

def let_state(xml):
    stt = ET.Element('letStatement')

    for item in xml:
        temp = ET.SubElement(stt, item.tag)
        temp.text = item.text

    return stt

def if_state(xml):
    stt = ET.Element('ifStatement')

    for item in xml:
        temp = ET.SubElement(stt, item.tag)
        temp.text = item.text

    return stt

def while_state(xml):
    stt = ET.Element('whileStatement')

    for item in xml:
        temp = ET.SubElement(stt, item.tag)
        temp.text = item.text

    return stt

def do_state(xml):
    stt = ET.Element('doStatement')

    for item in xml:
        temp = ET.SubElement(stt, item.tag)
        temp.text = item.text

    return stt

def return_state(xml):
    stt = ET.Element('returnStatement')

    for item in xml:
        temp = ET.SubElement(stt, item.tag)
        temp.text = item.text

    return stt
