import unittest

def func7(n):
    mas = []

    for i in range(int(n ** 0.5) + 1):
        if n >= i ** 2:
            mas.append(i)
            n -= i ** 2

    if n != 0:
        return 'It is impossible'
    else:
        return mas[1:]

#print(func7(1))


class TestFunc4(unittest.TestCase):

    def test1(self):
        self.assertEqual(func7(5), [1, 2])

    def test2(self):
        self.assertEqual(func7(14), [1, 2, 3])

    def test3(self):
        self.assertEqual(func7(0), [])

    def test4(self):
        self.assertEqual(func7(1), [1])

    def test5(self):
        self.assertEqual(func7(15), 'It is impossible')

if __name__ == '__main__':
    unittest.main()