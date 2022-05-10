import unittest
from check_pwd import check_pwd


class TestClass(unittest.TestCase):
    # Check if empty string returns False
    def test_01(self):
        a = ''
        self.assertFalse(check_pwd(a))

    # Check if valid length 8 strings return True
    def test_02(self):
        a = 'Abcd123!'
        self.assertTrue(check_pwd(a))

    # Check if a valid string with lowercase letters returns True
    def test_03(self):
        a = 'jK123456!'
        self.assertTrue(check_pwd(a))

    # Check if a valid string with uppercase and lowercase letters returns True
    def test_04(self):
        a = 'just4Fun!'
        self.assertTrue(check_pwd(a))

    # Check if a string missing digits returns False
    def test_05(self):
        a = '**Wowwhat@da@YitIs**'
        self.assertFalse(check_pwd(a))

    # Check if a string with valid symbols returns True
    def test_06(self):
        a = 'SummerIsS00n!'
        self.assertTrue(check_pwd(a))


if __name__ == '__main__':
    unittest.main()
