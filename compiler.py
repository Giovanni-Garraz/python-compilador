def compile_to_python(ast):
    code = []


    for node in ast:

        if node[0] == "assign":
            _, var, value = node
            code.append(f"{var} = {value}")

        elif node[0] == "print":
            _, left, op, right = node
            code.append(f"print({left}, {op}, {right})")

    return "\n".join(code)

