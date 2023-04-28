import re

class Regex:
    def __init__(self, input_string):
        self.input_string = input_string
        self.operators = ['NUM','PLUS','MINUS','STAR','SLASH']
    
    def scan(self):
        tokens = []
        regex = r"\d+|\+|\-|\*|\/"
        matches = re.findall(regex, self.input_string)
        for match in matches:
            if match.isdigit():
                tokens.append(('NUM', match))
            elif match == '+':
                tokens.append(('PLUS', match))
            elif match == '-':
                tokens.append(('MINUS', match))
            elif match == '*':
                tokens.append(('STAR', match))
            elif match == '/':
                tokens.append(('SLASH', match))
            else:
                raise ValueError(f'Unexpected character: {match}')
        return tokens

    def rpn(self,tokens):
        stack = []
        
        for token in tokens:
            if token[0] == 'NUM':
                stack.append(int(token[1]))
            elif token[0] in self.operators:
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
    input_string = file.read()
    regex = Regex(input_string)
    tokens = regex.scan()
    for token in tokens:
        print(f"Token [type={token[0]}, lexeme={token[1]}]")
    saida = regex.rpn(tokens)
    print()
    print("Saida: " + str(saida))


    
