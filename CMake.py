from compiler_tools.preprocess import *



class CMakeClass:
    def __init__(self, code_path):
        self.__codePath = code_path

    def build(self):
        self.__preprocess_text = Preprocessor(self.__codePath)
