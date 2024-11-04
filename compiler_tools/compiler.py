import os
import json
import pandas as pd
import re

# error class
class CompilerErorr(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

    def __str__(self):
        return repr(self.message)


class Compiler:
    def __init__(self, clean_text):
        self.id_num = 1
        self.id_dict = {

        }
        self.symbols = {
            ';': '<SEMICOLON_TK>',
            '(': '<PHARANTESES1_TK>',
            ')': '<PHARANTESES2_TK>',
            '{': '<BRACKET1_TK>',
            '}': '<BRACKET2_TK>',
        }

        self.operators = {
            '+': '<SUM_TK>',
            '-': '<SUB_TK>',
            '/': '<DIV_TK>',
            '*': '<MUL_TK>',
            '==': '<EQ_TK>',
            '>': '<BIG_TK>',
            '>=': '<BIGEQ_TK>',
            '<=': '<LOWEQ_TK>',
            '<': '<LOW_TK>',
            '++': '<INCREASE_TK>',
            '--': '<DECREASE_TK>',
            '=': '<ASIGN_TK>',
        }

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
        def adder(temp):
            if not temp: return
            if temp[0] == '"' or temp[-1] == '"':
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('string_constant')
                self.__SYMBOL_TABLE['Token'].append(f'<STR_TK>')
            elif temp[0] == "'" or temp[-1] == "'":
                if len(temp.replace("'", '')) != 1:
                    raise CompilerErorr(f"Invalid character len at {temp}")
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('char_constant')
                self.__SYMBOL_TABLE['Token'].append(f'<CHAR_TK>')
            elif temp in self.keywords:
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('keyword')
                self.__SYMBOL_TABLE['Token'].append(f'<{self.tokens[self.keywords.index(temp)]}>')
            elif temp in self.symbols:
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('symbol')
                self.__SYMBOL_TABLE['Token'].append(self.symbols[temp])
            elif temp in self.operators:
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('operators')
                self.__SYMBOL_TABLE['Token'].append(self.operators[temp])
            elif re.search(r'\d+\.\d+', temp) and not re.search(r'[^0-9\.]', temp):
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('float')
                self.__SYMBOL_TABLE['Token'].append('<FLOAT_CONST>')
            elif re.search(r'\d+', temp) and not re.search(r'[^0-9]', temp):
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('integer')
                self.__SYMBOL_TABLE['Token'].append('<INT_CONST>')
            elif (re.search(r'^[^0-9].*', temp) or re.search(r'^_.*', temp)) and not re.search(r'[^a-zA-Z0-9_]', temp):
                self.__SYMBOL_TABLE['Code'].append(temp)
                self.__SYMBOL_TABLE['Type'].append('identifier')
                if temp in self.id_dict.keys():
                    self.__SYMBOL_TABLE['Token'].append(f'<ID_TK, {self.id_dict[temp]}>')
                else:
                    self.__SYMBOL_TABLE['Token'].append(f'<ID_TK, {self.id_num}>')
                    self.id_dict[temp] = self.id_num
                    self.id_num += 1
            else:
                raise CompilerErorr(f'Unrecognized identifier: {temp}')

        codetxt = self.source_code

        control = None
        temp = ''
        for i in codetxt:
            if i == '"':  # string control
                temp += i
                if control == 'C': continue
                elif control == 'S':control = ''
                else: control = 'S'
            elif i == "'":  # char control
                temp += i
                if control == 'S': continue
                elif control == 'C': control = ''
                else: control = 'C'
            elif control:
                temp += i
            elif i in self.symbols.keys() or i in self.operators.keys():
                adder(temp)
                adder(i)
                temp = ''
            elif i in ['\n', ' ']:  # enter control
                adder(temp)
                temp = ''
            else:
                temp += i

        adder(temp)
        pd.DataFrame(self.__SYMBOL_TABLE).to_excel('final.xlsx', index=False)





















