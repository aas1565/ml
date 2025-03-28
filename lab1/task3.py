import unittest


def func3(a):
    if a < 0:
        return 0
    elif a == 1 or a == 0:
        return 1
    else:
        return bin(a).count('1')


num = input()
if num != '':
    res = func3(int(num))
    print(res)
else:
    print(0)


class TestFunc1(unittest.TestCase):

    def test1(self):
        self.assertEqual(func3(0), 1)

    def test2(self):
        self.assertEqual(func3(1), 1)

    def test3(self):
        self.assertEqual(func3(-1), 0)

    def test4(self):
        self.assertEqual(func3(5), 2)


if __name__ == '__main__':
    unittest.main()