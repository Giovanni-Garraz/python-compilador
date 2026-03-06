def parse(tokens):
    ast = []
    i = 0

    while i < len(tokens):

        token_type, token_value = tokens[i]


        if token_type == "LET":
            var_name = tokens[i+1][1]
            value = tokens[i+3][1]

            ast.append(("assign", var_name, value))
            i += 4


        elif token_type == "PRINT":
            left = tokens[i+1][1]
            op = tokens[i+2][1]
            right = tokens[i+3][1]

            ast.append(("print", left, op, right))
            i += 4

        else:
            raise SyntaxError("Erro de sintaxe")

    return ast
