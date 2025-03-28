import unittest

def func8(n):
    s=str(n)
    length=len(s)
    if length==1:
        return False
    if length%2 ==0:
        sum1=0
        sum2=0
        mid1=length//2-1
        mid2=length//2
        for i in range(0, mid1+1):
           sum1+=int(s[i])
        for i in range(mid2, length):
           sum2+=int(s[i])
        return sum1==sum2
    else:
        mid=length//2
        sum1=0
        sum2=0
        for i in range(0, mid):
           sum1+=int(s[i])
        for i in range(mid+1, length):
           sum2+=int(s[i])
        return sum1 == sum2

#print(func8(1001))

class TestFunc4(unittest.TestCase):

    def test1(self):
        self.assertEqual(func8(123321), True)

    def test2(self):
        self.assertEqual(func8(12345), False)

    def test3(self):
        self.assertEqual(func8(1234321), True)

    def test4(self):
        self.assertEqual(func8(1), False)

    def test5(self):
        self.assertEqual(func8(1001), True)

if __name__ == '__main__':
    unittest.main()