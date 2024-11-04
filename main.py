from CMake import CMakeClass
import os

# for directory in os.listdir("testfiles"):
#     for filename in os.listdir(os.path.join("testfiles", directory)):
#         try:
#             x = CMakeClass(os.path.join("testfiles", directory, filename))
#             x.build()
#         except Exception as err:
#             print(filename, '\t', err)



x = CMakeClass(os.path.join("testfiles", 'valid', 'all.c'))
x.build()


