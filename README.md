
---

# C Compiler writed with python

## Overview

This project is a custom compiler for the C programming language, designed to parse and transform C source code through each fundamental compilation stage. This compiler includes modules for **preprocessing**, **lexical analysis**, and aims to implement further stages like syntax analysis, semantic analysis, optimization, and code generation. Currently, the project includes the first version of the **Preprocessing** and **Lexical Analysis** stages.
*NOTICE: preprocessing and lexical analyzer writed for simple C codes and in next updates, it will improve for complex codes.*

## Features

- **Preprocessing**: 
  - Handles initial transformations by removing comments, processing macros, and including files.
  - The current version supports [mention any specific preprocessing details, like basic macro expansion or conditional compilation].

- **Lexical Analysis**:
  - Scans the source code to break it into tokens, identifying keywords, identifiers, operators, and symbols according to C’s syntax.
  - Outputs a tokenized form of the source code to be used in the syntax analysis stage.

- **Planned Stages**:
  - **Syntax Analysis**: Create a parse tree from tokens to represent the grammatical structure of the source code.
  - **Semantic Analysis**: Check for logical consistency, type checking, and correct usage of declarations and definitions.
  - **Optimization**: Optional stage to enhance the code’s performance by optimizing expressions, loops, and other constructs.
  - **Code Generation**: Translate the intermediate representation of the source code into machine code or an executable format.

## Project Structure

- **compiler tools**: this folder is main part of compiler that contain:
  - `data`: this folder contain keywords of language that it can find in the source code
  - `compiler.py`: compiler file that contain lexical analyzer, syntax analyzer and etc.
  - `preprocess.py`: process macros and comment clear is this part.
- **libraries**: library folder that contain library detials.
- **testfiles**: contain test codes that will use for validations
- **CMake.py**: controlling class that run compiler tools in order

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/your-c-compiler.git

```
write your code and give path of source code in the main file.

```python
from CMake import CMakeClass
import os
x = CMakeClass(os.path.join("testfiles", 'valid', 'all.c'))
```
and you can build it.

```python
x.build()
```

**if your code it true for preprocessing and lexical analyzer, it will give you oen final.xlsx file that contain tokenize of your code.**

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest new features. Please include test cases for new features or fixes.
