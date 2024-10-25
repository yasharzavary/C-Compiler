"""
this will process our code and get needed parts for compile.
"""

import re
import os
import json

class PreprocessError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
    def __str__(self):
        return repr(self.message)


class Preprocessor:
    def __init__(self):
        pass


    def read_libraries(self, path):
        file_txt = open(path, 'r').read().split('\n')
        print(file_txt)
        match = [find[0] for find in [re.findall(r'^\s*#include\s*<(.*)>\s*', line) for line in file_txt] if find]
        if match:
            lib_names = [re.findall(r'(.*)\..*', name)[0] for name in match]
            if not lib_names:
                lib_name = match.group(1)
            if not os.path.isfile(os.path.join('..', 'libraries', lib_name, '.json')):
                raise PreprocessError(f'{lib_name} doesn\'t exist in libraries')
            else:
                with (open(os.path.join('..', 'libraries', lib_name, '.json'), 'r') as lk,
                      open('data/coreKeywords.json') as ck):
                    l_keywords = json.load(lk)
                    c_keywords = json.load(ck)


if __name__ == '__main__':
    p = Preprocessor()
    p.read_libraries(os.path.join('..', 'testfiles', 'valid', 'all.c'))




