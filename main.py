from lexer import lexer
from parser import parse
from compiler import compile_to_python

with open("programa.txt", "r") as file:
    code = file.read()

tokens = lexer(code)

ast = parse(tokens)

python_code = compile_to_python(ast)

print("Código gerado:\n")
print(python_code)

with open("output.py", "w") as file:
    file.write(python_code)

print("Arquivo outout.py gerado com sucesso!")
