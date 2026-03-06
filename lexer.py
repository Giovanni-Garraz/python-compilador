import re

TOKENS = [
    ("LET", r"let"),
    ("PRINT", r"print"),
    ("NUMBER", r"\d+"),
    ("IDENTIFIER", r"[a-zA-Z_]\w*"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULT", r"\*"),
    ("DIV", r"/"),
    ("EQUALS", r"="),
 ]

def lexer(code):
    tokens = []

    lines = code.split("\n")
    for line in lines:
        words = line.split()


    for word in words:
        matched = False

        for token_name, pattern in TOKENS:
            if re.fullmatch(pattern, word):
                tokens.append((token_name, word))
                matched = True
                break

        if not matched:
            raise SyntaxError(f"Unknown desconhecido: {word}")

    return tokens