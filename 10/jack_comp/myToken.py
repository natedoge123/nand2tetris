import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

def token_string(s):
    token_items = []
    word = ''
    inside_string = False

    for char in s:
        if char == '"':
            if inside_string:
                if word:
                    token_items.append(word)
                    word = ''
                inside_string = False
            else:
                if word:
                    token_items.append(word)
                    word = ''
                inside_string = True
        elif inside_string:
                word += char
        elif char.isalpha():
            word += char
        else:
            if word:
                token_items.append(word)
                word = ''
            if char != ' ':
                token_items.append(char)
    if word:
        token_items.append(word)

    return token_items

def normal_token(s):
    token_items = []
    word = ''
    for char in s:
        if char.isalpha():
            word += char
        else:
            if word:
                token_items.append(word)
                word = ''
            if char != ' ':
                token_items.append(char)
    if word:
        token_items.append(word)

    return token_items

def merge_quotes(lst):
    merged_list = []
    merge_flag = False
    merged_entry = ''

    for entry in lst:
        if entry == '"':
            if merge_flag:
                merged_list.append(merged_entry)
                merged_entry = ''
                merge_flag = False
            else:
                merge_flag = True
        
        elif merge_flag:
            if merged_entry:
                merged_entry += ' '
            merged_entry += entry
        else:
            merged_list.append(entry)

    return merged_list


def tokenizer(lst):
    simple = token_string(lst)
    nw = [item for item in simple if item != "\n"]
    nt = [item for item in nw if item != "\t"]
    merged = merge_quotes(nt)
    return merged

def xmlToken(lst):
    keyword_list = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
    symbol_list = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*''/', '&', '|', '<', '>', '=', '~']

    root = ET.Element('token')
    for item in lst:
        if item in keyword_list:
            temp = ET.SubElement(root, 'keyword')
            temp.text = item
        elif item in symbol_list:
            temp = ET.SubElement(root, 'symbol')
            temp.text = item
        elif item.isnumeric():
            temp = ET.SubElement(root, 'integerConstant')
            temp.text = item
        elif (item[0].isnumeric() != True) and (' ' not in item):
            temp = ET.SubElement(root, 'identifier')
            temp.text = item
        elif (item[0].isnumeric() != True) and (' ' in item):
            temp = ET.SubElement(root, 'stringConstant')
            temp.text = item

    return(xmlIndent(root))


def xmlIndent(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="    ")


