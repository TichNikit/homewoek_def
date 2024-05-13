#Создайте новую функцию def test...
#Создайте две переменные a и b внутри пространства имен функции test
#Распечатайте a и b внутри функции test
#Создайте функцию def test2 с тремя параметрами, функция должна распечатывать все три параметра внутри своего тела

def test():
    a = 'my'
    b = 'name'
    print(a, b)

def test2(a = 'My name', b = 'is', c = 'Nikita'):
    print(a, b, c)

test()

test2('my last name', 'is', 'Ivanov')
