def input_data():
    print('Введите начальное значение корня:')
    x = float(input())
    print('Введите корень искомого числа')
    y = float(input())
    return x, y

def main():
    x, y = input_data()
    buffer = None  # none ничего
    while x != buffer:
        buffer = x  # копия переменной x
        x = (1 / 2) * (x + (y / x))
    return x

if __name__ == "__main__":
    print(main())
