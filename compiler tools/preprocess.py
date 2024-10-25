"""
this will process our code and get needed parts for compile.
"""

import re
import os

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
        file_txt = open(path, 'r').read()
        match = re.search(r'#include <(.*)>', file_txt)
        if match:
            lib_name = re.search(r'(.*)\..*',match.group(1))
            if not lib_name:
                lib_name = match.group(1)
            if not os.path.isfile(os.path.join('..', 'libraries', lib_name, '.json')):
                raise PreprocessError(f'{lib_name} doesn\'t exist in libraries')
            else:
                with (open(os.path.join('..', 'libraries', lib_name, '.json'), 'r') as lk,
                      open('data/coreKeywords.json') as ck):
                    pass



