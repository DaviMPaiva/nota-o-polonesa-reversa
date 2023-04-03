def rpn(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            y, x = stack.pop(), stack.pop()
            if token == '+':
                stack.append(x + y)
            elif token == '-':
                stack.append(x - y)
            elif token == '*':
                stack.append(x * y)
            elif token == '/':
                stack.append(x // y)
    return stack.pop()

with open('Calc1.stk') as file:
    tokens = file.read().split()
    result = rpn(tokens)

print("Saida: "+ str(result))
