import unittest

def func2(string):
    dict1 = {}
    if not string:
        return False
    for i in string.lower():
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    for value in dict1.values():
        if value > 1:
            return False
    return True

class TestFunc1(unittest.TestCase):

    def test1(self):
        self.assertEqual(func2(""), False)

    def test2(self):
        self.assertEqual(func2("aa"), False)

    def test3(self):
        self.assertEqual(func2("awer"), True)

# Запуск кода только если файл запускается как основной
if __name__ == '__main__':
    #a = input("Введите строку: ")
    #res = func2(a)
    #print(res)
    unittest.main()
