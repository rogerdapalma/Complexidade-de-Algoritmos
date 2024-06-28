import re

# Função para análise léxica do código C, identificando tokens como números, operadores e identificadores.
def lexer(code):
    tokens = []
    token_specification = [
        ('NUMBER', r'\d+(\.\d*)?'),   # Números inteiros e ponto flutuante
        ('ASSIGN', r'='),             # Operador de atribuição
        ('END', r';'),                # Fim de linha (ponto e vírgula)
        ('ID', r'[A-Za-z_]\w*'),      # Identificadores (variáveis)
        ('OP', r'[+\-*/]'),           # Operadores aritméticos
        ('NEWLINE', r'\n'),           # Nova linha
        ('SKIP', r'[ \t]+'),          # Espaços e tabulações (ignorados)
        ('MISMATCH', r'.'),           # Qualquer outro caractere não esperado
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_number = 1
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in ('int', 'float'):
            kind = value.upper()
        elif kind == 'NEWLINE':
            line_number += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_number}')
        tokens.append((kind, value))
    return tokens

# Função para gerar código intermediário a partir dos tokens identificados.
def generate_intermediate_code(tokens):
    intermediate_code = []
    current_decl_type = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token[0] in ('INT', 'FLOAT'):  # Identifica declaração de tipos
            current_decl_type = token[0].lower()
        elif token[0] == 'ID' and tokens[i + 1][0] == 'ASSIGN':  # Processa atribuições e operações
            if tokens[i - 1][0] in ('INT', 'FLOAT'):
                intermediate_code.append(f"DECL {current_decl_type} {token[1]} = {tokens[i + 2][1]};")
                i += 3  # Pula os tokens de atribuição e valor
            else:
                j = i + 2
                while j < len(tokens) and tokens[j][0] != 'END':
                    j += 1
                if j - i == 3:
                    intermediate_code.append(f"{token[1]} = {tokens[i + 2][1]};")
                elif j - i > 3:  # Trata operações com dois operandos
                    op = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}[tokens[i + 3][1]]
                    intermediate_code.append(f"{op} {token[1]}, {tokens[i + 2][1]}, {tokens[i + 4][1]};")
                i = j
        i += 1
    return intermediate_code

def main():
    input_filename = 'codigo_fonte.c'
    output_filename = 'Resultado.txt'

    try:
        with open(input_filename, 'r') as file:
            codigo_fonte_content = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{input_filename}' não encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo '{input_filename}': {e}")
        return

    tokens = lexer(codigo_fonte_content)
    intermediate_code = generate_intermediate_code(tokens)

    with open(output_filename, 'w') as file:
        for line in intermediate_code:
            print(line)
            file.write(line + '\n')
    print("Código intermediário gerado com sucesso!")

if __name__ == '__main__':
    main()
