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

    def build(self):
        self.__comment_clear()
        self.__read_libraries()
        return self.__codeText

    def __comment_clear(self):
        temp = self.__codeText
        # find comment patterns in the code
        comments = re.findall(r'/{2}.*\n', temp) + ['second'] + re.findall(r'(?<=[^\"])/\*.*?\*/',
                                                                           temp, re.DOTALL) + ['third'] + re.findall(r'^/\*.*?\*/',
                                                                                                                     temp, re.DOTALL)
        for comment in comments:
            temp = temp.replace(comment, '')

        self.__codeText = temp


    def __read_libraries(self):
        file_txt = self.__codeText
        libraries = list(re.findall(r'#include\s*<(.*).h>\s*', file_txt))
        coreKeywords = json.load(open('compiler_tools/data/coreKeywords.json', 'r'))['keywords']  # read list of keywords.
        keyword_temp = list()
        library_file_address = 'libraries/'

        for lib in libraries:
            if not os.path.exists(library_file_address + lib + '.json'):
                raise PreprocessError(f'{lib} doesn\'t exist')
            else:
                keyword_temp += json.load(open(library_file_address + lib + '.json'))['keywords']

        finalKeywordList = {'keywords':keyword_temp + coreKeywords}  # list of keywords.
        with open('compiler_tools/data/finalKeywords.json', 'w') as outfile:
            json.dump(finalKeywordList, outfile, indent=6)






