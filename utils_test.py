from utils import utils
import unittest


class Testutils(unittest.TestCase):
    def test_utils_reverse(self):
        self.assertRaises(TypeError, utils.reversed, '123')
        self.assertRaises(TypeError, utils.reversed, 123.0)
        self.assertEqual(utils.reversed(123), 321)

    def test_utlils_formater(self):
        self.assertRaises(TypeError, utils.formater, '123')
        self.assertRaises(TypeError, utils.formater, 123.0)
        self.assertEqual(utils.formater(123), ['0b1111011', '0o173'])


if __name__ == "__main__":
    print("Testing utils.py")
    unittest.main()
    print("Everything passed")
