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
    def __init__(self, path):
        self.__codeText = open(path, 'r').read()


    def comment_clear(self):
        temp = self.__codeText
        # find comment patterns in the code
        comments = re.findall(r'/{2}.*\n', temp) + ['second'] + re.findall(r'(?<=[^\"])/\*.*?\*/', temp, re.DOTALL) + ['third'] + re.findall(r'^/\*.*?\*/', temp, re.DOTALL)
        print(comments)
        for comment in comments:
            temp = temp.replace(comment, '')

        self.__codeText = temp


    def read_libraries(self, path):
        file_txt = open(path, 'r').read().split('\n')
        # if re.search(r'')
        match = [find[0] for find in [re.findall(r'#include\s*<(.*)>\s*', line) for line in file_txt] if find]
        if match:
            lib_names = list()
            for name in match:
                if not re.search('.h', name):
                    pass

            lib_names = [
                re.findall(r'(.*)\..*', name)[0] if re.findall(r'(.*)\..*', name) else (_ for _ in ()).throw(
                    PreprocessError(f'undefinded library {name}'))
                for name in match
            ]
            print(lib_names)
            if not os.path.isfile(os.path.join('..', 'libraries', lib_names, '.json')):
                raise PreprocessError(f'{lib_names} doesn\'t exist in libraries')
            else:
                with (open(os.path.join('..', 'libraries', lib_names, '.json'), 'r') as lk,
                      open('data/coreKeywords.json') as ck):
                    l_keywords = json.load(lk)
                    c_keywords = json.load(ck)


if __name__ == '__main__':
    p = Preprocessor(os.path.join('..', 'testfiles', 'valid', 'all.c'))
    p.comment_clear()




