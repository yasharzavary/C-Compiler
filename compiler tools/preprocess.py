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
        comments = re.findall(r'/{2}.*\n', temp) + ['second'] + re.findall(r'(?<=[^\"])/\*.*?\*/',
                                                                           temp, re.DOTALL) + ['third'] + re.findall(r'^/\*.*?\*/',
                                                                                                                     temp, re.DOTALL)
        for comment in comments:
            temp = temp.replace(comment, '')

        self.__codeText = temp


    def read_libraries(self):
        file_txt = self.__codeText
        print(file_txt)
        libraries = list(re.findall(r'#include\s*<(.*).h>\s*', file_txt))
        coreKeywords = json.load(open('data/coreKeywords.json', 'r'))['keywords']  # read list of keywords.
        keyword_temp = list()
        library_file_address = os.path.join('..', 'libraries') + '/'

        for lib in libraries:
            if not os.path.exists(library_file_address + lib + '.json'):
                raise PreprocessError(f'{lib} doesn\'t exist')
            else:
                keyword_temp += json.load(open(library_file_address + lib + '.json'))['keywords']

        finalKeywordList = keyword_temp + coreKeywords  # list of keywords.
        print(finalKeywordList)

if __name__ == '__main__':
    p = Preprocessor(os.path.join('..', 'testfiles', 'valid', 'all.c'))
    p.comment_clear()
    p.read_libraries()




