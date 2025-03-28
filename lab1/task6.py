import unittest

def func6(n):
    factors = {}

    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i

    if n > 2:
        factors[n] = 1

    result = []
    for prime, power in factors.items():
        if power > 1:
            result.append(f"({prime}**{power})")
        else:
            result.append(f"({prime})")

    return ''.join(result)


#print(prime_factors(81))

class TestFunc4(unittest.TestCase):

    def test1(self):
        self.assertEqual(func6(86240), "(2**5)(5)(7**2)(11)")

    def test2(self):
        self.assertEqual(func6(60), "(2**2)(3)(5)")

    def test3(self):
        self.assertEqual(func6(101), "(101)")

    def test4(self):
        self.assertEqual(func6(1), "")

    def test5(self):
        self.assertEqual(func6(100), "(2**2)(5**2)")

if __name__ == '__main__':
    unittest.main()
