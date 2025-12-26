def calculate_rpn(expression):
    """
    Вычисляет выражение в обратной польской нотации с поддержкой унарных операторов
    """
    stack = []
    tokens = expression.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        is_unary = False
        if token in ('+', '-'):
            if i == 0 or (i > 0 and tokens[i - 1] in ('+', '-', '*', '/', '^')):
                if i + 1 < len(tokens):
                    next_token = tokens[i + 1]
                    is_next_number = False
                    if next_token.replace('.', '', 1).replace('-', '', 1).isdigit():
                        is_next_number = True
                    elif next_token[0] == '-' and next_token[1:].replace('.', '', 1).isdigit():
                        is_next_number = True
                    elif next_token[0] == '+' and next_token[1:].replace('.', '', 1).isdigit():
                        is_next_number = True
                    elif next_token.replace('.', '', 1).isdigit():
                        is_next_number = True
                    if is_next_number:
                        is_unary = True
        if is_unary:
            i += 1
            if i >= len(tokens):
                raise ValueError(f"Недостаточно операндов для унарного оператора {token}")
            num_token = tokens[i]
            try:
                if num_token[0] == '+':
                    num_token = num_token[1:]
                num = float(num_token)
                if token == '-':
                    num = -num
                stack.append(num)
            except ValueError:
                raise ValueError(f"После унарного оператора ожидается число: {num_token}")
            i += 1
            continue
        if (token.replace('.', '', 1).isdigit() or (token[0] == '-' and token[1:].replace('.', '', 1).isdigit()) or (token[0] == '+' and token[1:].replace('.', '', 1).isdigit())):
            if token[0] == '+':
                token = token[1:]
            try:
                stack.append(float(token))
            except ValueError:
                pass
            else:
                i += 1
                continue
        if token in ('+', '-', '*', '/', '^'):
            if len(stack) < 2:
                raise ValueError(f"Недостаточно операндов для оператора {token}")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Деление на ноль")
                result = a / b
            elif token == '^':
                result = a ** b
            stack.append(result)
        else:
            raise ValueError(f"Неизвестный оператор или некорректный токен: {token}")

        i += 1
    if len(stack) != 1:
        raise ValueError("Некорректное выражение")
    return stack[0]

def main():
    print("Калькулятор обратной польской нотации (RPN) \n Для выхода введите quit ")
    while True:
        try:
            print("\n Введите выражение RPN")
            user_input = input().strip()
            if user_input.lower() == 'quit':
                print("Выход")
                break
            if not user_input:
                continue
            result = calculate_rpn(user_input)
            print("Результат", int(result))
        except Exception as e:
            print(f"Ошибка  {e}")
if __name__ == "__main__":
    main()