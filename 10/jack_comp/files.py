import glob
import os
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

def open_dir(dir_path):
    file_type = "*.jack"
    file_paths = glob.glob(dir_path + "/" + file_type)

    path_list = []

    for path in file_paths:
        path_list.append(path)

    return path_list

def read_files(open_file):
    lines = []
    with open(open_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = re.sub(r'//.*?\n', '\n', line)
            if line.strip():
                if not line.startswith('/'):
                        lines.append(line.strip())
        content = ''.join(lines)
        content = remove_comments(content)
            
    return content

def remove_comments(code):
    lines = code.split('\n')
    cleaned_code = []
    inside_block_comment = False
    for line in lines:
        # Check for /* and */ comments
        if '/*' in line and '*/' in line:
            line = line.split('/*')[0] + line.split('*/')[1]
        elif '/*' in line:
            inside_block_comment = True
            line = line.split('/*')[0]
        elif '*/' in line:
            inside_block_comment = False
            line = line.split('*/')[1]
        elif inside_block_comment:
            line = ''

        # Check for /** and */ comments
        if '/**' in line and '*/' in line:
            line = line.split('/**')[0] + line.split('*/')[1]
        elif '/**' in line:
            inside_block_comment = True
            line = line.split('/**')[0]
        elif '*/' in line:
            inside_block_comment = False
            line = line.split('*/')[1]
        elif inside_block_comment:
            line = ''

        # Remove inline comments starting with //
        line = line.split('//')[0].rstrip()

        # Append the cleaned line to the cleaned_code list
        cleaned_code.append(line)

    return '\n'.join(cleaned_code)

def write_file(content, file_path, extension):
    save_path = file_path + '.' + extension
    with open(save_path, 'w') as file:
        file.write(content)

def explode_path(file_path):
    pth = Path(file_path)
    return [str(part) for part in pth.parts]
       


