#!/usr/bin/python
import os
import argparse
from time import localtime, strftime, strptime

C_MAKEFILE = 'all:' \
             '\n\t%s -O2 %s.cpp -o run' \
             '\n' \
             '\nclean:' \
             '\n\t rm run'

JAVA_MAKEFILE = 'all:' \
                '\n\tjavac %s.java' \
                '\n' \
                '\nrun:' \
                '\njava %s' \
                '\n' \
                '\nclean:' \
                '\n\t rm %s'

C_HEADER = '/*' \
           '\n    ID: Shidfar1' \
           '\n    TASK: {}' \
           '\n    LANG: {}' \
           '\n*/'

JAVA_HEADER = '/*' \
              '\n    ID: Shidfar1' \
              '\n    LANG: {}' \
              '\n    TASK: {}' \
              '\n*/'

PASCAL_HEADER = '{' \
                '\n    ID: Shidfar1' \
                '\n    TASK: %s' \
                '\n    LANG: %s' \
                '\n}'

PYTHON_HEADER = '"""' \
                '\nID: Shidfar1' \
                '\nLANG: {}' \
                '\nTASK: {}' \
                '\n"""'

C_BODY = '\n' \
         '\n#include <stdio.h>' \
         '\n#include <stdlib.h>' \
         '\n' \
         '\nvoid main ()' \
         '\n{' \
         '\n    FILE *fin  = fopen ("%s.in", "r");' \
         '\n    FILE *fout = fopen ("%s.out", "w");' \
         '\n    ' \
         '\n    exit (0);' \
         '\n}'

CPP_BODY = '\n' \
           '\n#include <iostream>' \
           '\n#include <fstream>' \
           '\n#include <string>' \
           '\n' \
           '\nusing namespace std;' \
           '\n' \
           '\nint main() {' \
           '\n    ofstream fout ("%s.out", std::ios::out);' \
           '\n    ifstream fin ("%s.in", std::ios::in);' \
           '\n    ' \
           '\n    return 0;' \
           '\n}'

JAVA_BODY = '\n' \
            '\nimport java.io.*;' \
            '\nimport java.util.*;' \
            '\n' \
            '\nclass %s {' \
            '\n    public static void main (String [] args) throws IOException {' \
            '\n        // Use BufferedReader rather than RandomAccessFile; it\'s much faster' \
            '\n        BufferedReader f = new BufferedReader(new FileReader("%s.in"));' \
            '\n                                                      // input file name goes above' \
            '\n        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("%s.out")));' \
            '\n        // Use StringTokenizer vs. readLine/split -- lots faster' \
            '\n//        StringTokenizer st = new StringTokenizer(f.readLine());' \
            '\n//                                                      // Get line, break into tokens' \
            '\n//        int i1 = Integer.parseInt(st.nextToken());    // first integer' \
            '\n//        int i2 = Integer.parseInt(st.nextToken());    // second integer' \
            '\n//        out.println(i1+i2);                           // output result' \
            '\n        out.close();                                    // close the output file' \
            '\n    }' \
            '\n}'

PASCAL_BODY = '\n' \
              '\nProgram %s;' \
              '\nVar fin, fout: text;' \
              '\nBegin' \
              '\n    Assign(fin, \'%s.in\'); Reset(fin);' \
              '\n    Assign(fout, \'%s.out\'); Rewrite(fout);' \
              '\n    ' \
              '\n    Close(fout);' \
              '\nEnd'

PYTHON_BODY = '\n' \
              '\nfin = open (\'%s.in\', \'r\')' \
              '\nfout = open (\'%s.out\', \'w\')' \
              '\n# x,y = map(int, fin.readline().split())' \
              '\n# sum = x+y' \
              '\n# fout.write (str(sum) + \'\\n\')' \
              '\nfout.close()'


def c_composer(task, lang):
    compiler = 'gcc'
    header = C_HEADER.format(task, lang)
    body = C_BODY % (task, task)
    makefile = C_MAKEFILE % (compiler, task)
    return header, body, makefile


def cpp_composer(task, lang):
    compiler = 'g++'
    header = C_HEADER.format(task, lang)
    body = CPP_BODY % (task, task)
    makefile = C_MAKEFILE % (compiler, task)
    return header, body, makefile


def java_composer(task, lang):
    header = JAVA_HEADER.format(lang, task)
    body = JAVA_BODY % (task.title(), task, task)
    makefile = JAVA_MAKEFILE % (task, task, task)
    return header, body, makefile


def pascal_composer(task, lang):
    header = PASCAL_HEADER % (task, lang)
    body = PASCAL_BODY % (task.title(), task, task)
    makefile = ''
    return header, body, makefile


def python_composer(task, lang):
    header = PYTHON_HEADER.format(lang, task)
    body = PYTHON_BODY % (task, task)
    makefile = ''
    return header, body, makefile


LANG_DICT = {
    'cpp': {'Name': 'C++', 'Function': cpp_composer, 'Extension': 'cpp'},
    'c++': {'Name': 'C++', 'Function': cpp_composer, 'Extension': 'cpp'},
    'cpp11': {'Name': 'C++11', 'Function': cpp_composer, 'Extension': 'cpp'},
    'c++11': {'Name': 'C++11', 'Function': cpp_composer, 'Extension': 'cpp'},
    'cpp14': {'Name': 'C++14', 'Function': cpp_composer, 'Extension': 'cpp'},
    'c++14': {'Name': 'C++14', 'Function': cpp_composer, 'Extension': 'cpp'},
    'c': {'Name': 'C', 'Function': c_composer, 'Extension': 'c'},
    'python2': {'Name': 'PYTHON2', 'Function': python_composer, 'Extension': 'py'},
    'py2': {'Name': 'PYTHON2', 'Function': python_composer, 'Extension': 'py'},
    'python3': {'Name': 'PYTHON3', 'Function': python_composer, 'Extension': 'py'},
    'py3': {'Name': 'PYTHON3', 'Function': python_composer, 'Extension': 'py'},
    'python': {'Name': 'PYTHON3', 'Function': python_composer, 'Extension': 'py'},
    'py': {'Name': 'PYTHON3', 'Function': python_composer, 'Extension': 'py'},
    'java': {'Name': 'Java', 'Function': java_composer, 'Extension': 'java'},
    'jv': {'Name': 'Java', 'Function': java_composer, 'Extension': 'java'},
    'pascal': {'Name': 'PASCAL', 'Function': pascal_composer, 'Extension': 'pas'},
    'pa': {'Name': 'PASCAL', 'Function': pascal_composer, 'Extension': 'pas'},
    'ps': {'Name': 'PASCAL', 'Function': pascal_composer, 'Extension': 'pas'},
    'pas': {'Name': 'PASCAL', 'Function': pascal_composer, 'Extension': 'pas'}
}


def args_wrapper(task, lang):
    lower_lang = lang.lower()
    lower_task = task.lower()
    header = ""
    body = ""
    dir = "./" + lower_task
    source = dir + "/" + lower_task + "."
    input_file = dir + "/" + lower_task + ".in"
    output_file = dir + "/" + lower_task + ".out"
    makefile_path = dir + "/makefile"

    if LANG_DICT.get(lower_lang) is not None:
        composer = LANG_DICT.get(lower_lang)
        composer_name = composer['Name']
        composer_function = composer['Function']
        composer_extension = composer['Extension']
        source = source + composer_extension
        header, body, makefile = composer_function(lower_task, composer_name)
        return dir, source, input_file, output_file, header, body, makefile, makefile_path
    else:
        print("Language is not supported '{}'".format(lang))
        raise Exception


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument('command')
    parser.add_argument('-T', '--task', help='task name', required=True)
    parser.add_argument('-L', '--lang', help='language', required=True)
    args = parser.parse_args()

    # argument = args.argument
    task = args.task
    lang = args.lang

    # try:
    dir, source, input_file, output_file, header, body, makefile, makefile_path = args_wrapper(task, lang)
    # print(args_wrapper(task, lang))
    if not os.path.exists(dir):
        os.makedirs(dir)
    if os.path.exists(source):
        print("File already exists, remove it to continue...")
    else:
        with open(source, 'w') as f:
            f.write('{}{}'.format(header, body))
        with open(input_file, 'w') as f:
            f.write('\n')
        with open(output_file, 'w') as f:
            f.write('\n')
        with open(makefile_path, 'w') as f:
            f.write(makefile)
    # except Exception:
    #     print("General error while running code composer.")
    # else:
    #     print("Your file was successfully created.")


if __name__ == "__main__":
    exit(main())
