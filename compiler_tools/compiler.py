import os
import  json

# error class
class CompilerErorr(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

    def __str__(self):
        return repr(self.message)


class Compiler:
    def __init__(self, clean_text):
        self.__SYMBOL_TABLE = {
            'Code': list(),
            'Type': list(),
            'Token': list()
        }
        self.source_code = clean_text
        self.keywords = json.load(open('compiler_tools/data/finalKeywords.json', 'r'))['keywords']
        self.tokens = json.load(open('compiler_tools/data/finalKeywords.json', 'r'))['TOKENS']

    def build(self):
        self.__lexical_analysis()

    def __lexical_analysis(self):
        """
        main function to analyze lexically and send to next phase.
        :return: result of analyze
        """
        codetxt = self.source_code

        print(codetxt)

        control = None
        temp = ''
        for i in codetxt:
            if i == '"':  # string control
                temp += i
                if control == 'S':control = ''
                else: control = 'S'
            elif i == "'":  # char control
                temp += i
                if control == 'C': control = ''
                else: control = 'C'
            elif i == '\n':  # enter control
                if temp:
                    pass
                else: continue
            elif i == ' ':  # space control
                if control in ['S', 'C']:  # it is a char or string
                    temp += i
                elif temp:
                    print(f"-{temp}-")
                    if temp[0] == '"' or temp[-1] == '"':
                        self.__SYMBOL_TABLE['code'].append(temp)
                        self.__SYMBOL_TABLE['Type'].append('string_constant')
                        self.__SYMBOL_TABLE['Token'].append(f'<STR_TK, {temp}>')
                    elif temp[0] == "'" or temp[-1] == "'":
                        self.__SYMBOL_TABLE['code'].append(temp)
                        self.__SYMBOL_TABLE['Type'].append('char_constant')
                        self.__SYMBOL_TABLE['Token'].append(f'<CHAR_TK, {temp}>')
                    elif temp in self.keywords:
                        self.__SYMBOL_TABLE['Code'].append(temp)
                        self.__SYMBOL_TABLE['Type'].append('keyword')
                        self.__SYMBOL_TABLE['Token'].append(f'<{self.tokens[self.keywords.index(temp)]}>')

                    temp = ''

                else:
                    continue
            else:
                temp += i

        print(self.__SYMBOL_TABLE)




















