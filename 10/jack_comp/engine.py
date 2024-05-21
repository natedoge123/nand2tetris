import xml.etree.ElementTree as ET
from xml.dom import minidom

def runEngine(token): #takes tokenized xml tree and gives foramtted one
    
    return 0

def compClass():
    return 0

def compClassVarDec():
    return 0

def compSubRoutine():
    return 0

def compParameterList():
    return 0

def compVarDec():
    return 0

def compStatement():
    return 0

def compDo():
    return 0

def compLet():
    return 0

def compWhile():
    return 0

def compReturn():
    return 0

def compIf():
    return 0

def compExpression():
    return 0

def compTerm():
    return 0

def compExpressionList():
    return 0


def xmlPrint(xml):
    long_string = ET.tostring(xml, 'utf-8')
    indented = minidom.parseString(long_string)
    return indented.toprettyxml(indent="    ")





