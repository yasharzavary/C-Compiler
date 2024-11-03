import os

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
            if i == '\n':
                if temp:
                    pass
                else: continue

            elif i == ' ':
                if control in ['S', 'C']:  # it is a char or string
                    pass
                else:
                    continue
            else:
                temp += i






















