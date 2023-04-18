def scan(input_string):

    tokens = []

    i = 0
    for i in input_string:
        if i.isdigit():
            tokens.append(('NUM', i))
        elif i == '+':
            tokens.append(('PLUS', i))
        elif i == '-':
            tokens.append(('MINUS', i))
        elif i == '-':
            tokens.append(('SLASH', i))
        elif i == '*':
            tokens.append(('STAR', i))
        else:
            raise ValueError(f'Unexpected character: {i}')
    return tokens

def rpn(tokens):
    stack = []
    for token in tokens:
        if token[0] == 'NUM':
            stack.append(int(token[1]))
        elif token[0] == 'OP':
            y, x = stack.pop(), stack.pop()
            if token[1] == '+':
                stack.append(x + y)
            elif token[1] == '-':
                stack.append(x - y)
            elif token[1] == '*':
                stack.append(x * y)
            elif token[1] == '/':
                stack.append(x // y)
    return stack.pop()

with open('Calc1.stk') as file:
    input_string = file.read().split()
    tokens = scan(input_string)
    for i in tokens:
        print("Token [type="+i[0]+", lexeme="+i[1]+"]")

    saida = rpn(tokens)
    print()
    print("Saida: " + str(saida))

    
