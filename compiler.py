import os

# error class
class CompilerErorr(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

    def __str__(self):
        return repr(self.message)


class Compiler:
    def __init__(self, file_path):
        Compiler.is_exist(file_path)
        self.__SYMBOL_TABLE = {
            'Code': list(),
            'Type': list(),
            'Token': list()
        }
        self.source_code = self.file_read(file_path)

    @staticmethod
    def is_exist(file_path):
        if not os.path.exists(file_path):
            raise CompilerErorr('file doesn\'t exist, please recheck path address')

    def file_read(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()

    def __lexical_analysis(self):
        """
        main function to analyze lexically and send to next phase.
        :return: result of analyze
        """
        pass




















