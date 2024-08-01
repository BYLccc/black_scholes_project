import unittest
from black_scholes import black_scholes_call, black_scholes_put

class TestBlackScholesModel(unittest.TestCase):

    def test_call_option_price(self):
        S = 100
        X = 100
        T = 1
        r = 0.05
        sigma = 0.2
        expected_call_price = 10.45
        call_price = black_scholes_call(S, X, T, r, sigma)
        self.assertAlmostEqual(call_price, expected_call_price, places=2)

    def test_put_option_price(self):
        S = 100
        X = 100
        T = 1
        r = 0.05
        sigma = 0.2
        expected_put_price = 5.57
        put_price = black_scholes_put(S, X, T, r, sigma)
        self.assertAlmostEqual(put_price, expected_put_price, places=2)

    def test_different_parameters(self):
        S = 120
        X = 100
        T = 0.5
        r = 0.03
        sigma = 0.25
        expected_call_price = 22.44  # Use an online calculator to find the expected value
        expected_put_price = 0.73   # Use an online calculator to find the expected value
        call_price = black_scholes_call(S, X, T, r, sigma)
        put_price = black_scholes_put(S, X, T, r, sigma)
        self.assertAlmostEqual(call_price, expected_call_price, places=2)
        self.assertAlmostEqual(put_price, expected_put_price, places=2)

if __name__ == '__main__':
    unittest.main()
