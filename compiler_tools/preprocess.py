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
        jsonfile = json.load(open('compiler_tools/data/coreKeywords.json', 'r'))
        coreKeywords = jsonfile['keywords']  # read list of keywords.
        tokens = jsonfile['TOKENS']  # read list of keywords.
        keyword_temp = list()
        token_temp = list()
        library_file_address = 'libraries/'

        # loop on each library
        for lib in libraries:
            # check, if exist, add them to core keywords.
            if not os.path.exists(library_file_address + lib + '.json'):
                raise PreprocessError(f'{lib} doesn\'t exist')
            else:
                temp = json.load(open(library_file_address + lib + '.json'))
                keyword_temp += temp['keywords']
                token_temp += temp['TOKENS']


        # delete all include<library> parts
        for full_lib in re.findall(r'#include.*?\n', self.__codeText):
            self.__codeText = self.__codeText.replace(full_lib, '')


        finalKeywordList = {
            'keywords': coreKeywords + keyword_temp,
            'TOKENS': tokens + token_temp
        }  # list of keywords.
        with open('compiler_tools/data/finalKeywords.json', 'w') as outfile:
            json.dump(finalKeywordList, outfile, indent=6)






