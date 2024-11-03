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


    def __lexical_analysis(self):
        """
        main function to analyze lexically and send to next phase.
        :return: result of analyze
        """
        pass




















