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
        self.file_path = file_path


    @staticmethod
    def is_exist(file_path):
        if not os.path.exists(file_path):
            raise CompilerErorr('file doesn\'t exist, please recheck path address')














