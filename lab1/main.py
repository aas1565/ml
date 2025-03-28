import unittest

def func1(string):
  dict1= {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
  for i in string.lower():
    if i in dict1:
      dict1[i]+=1
    else:
      continue
  return dict1

#a= input()
#res=func1(a)
#print(res)


class TestFunc1(unittest.TestCase):

    def test1(self):
        self.assertEqual(func1(""), {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test2(self):
        self.assertEqual(func1("bcdfghjklmnpqrstvwxyz"), {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test3(self):
        self.assertEqual(func1("aeiou"), {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    def test4(self):
        self.assertEqual(func1("AbEcIdOfUg"), {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    def test5(self):
        self.assertEqual(func1("banana"), {'a': 3, 'e': 0, 'i': 0, 'o': 0, 'u': 0})

    def test6(self):
        self.assertEqual(func1("hello world"), {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0})

if __name__ == '__main__':
    unittest.main()



































































