import unittest

def func4(a):
    if a < 10:
        return 0
    count = 0
    while a >= 10:
        res = 1
        while a > 0:
            res *= a % 10
            a //= 10
        a = res
        count += 1

    return count

#num = input()
#if num!='':
    #res = func4(int(num))
    #print(res)
#else:
    #print(0)


class TestFunc4(unittest.TestCase):

    def test1(self):
        self.assertEqual(func4(4), 0)

    def test2(self):
        self.assertEqual(func4(39), 3)

    def test3(self):
        self.assertEqual(func4(999), 4)

    def test4(self):
        self.assertEqual(func4(123456), 2)

    def test5(self):
        self.assertEqual(func4(10), 1)

if __name__ == '__main__':
    unittest.main()