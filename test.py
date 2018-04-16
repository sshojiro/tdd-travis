# coding=utf-8

"""
This test code is inspired by python-louvain module in https://github.com/taynaud/python-louvain.
"""

import unittest
from module import parse_nums, trim_symbol

class ModuleTest(unittest.TestCase):
    """
    Tests for modules
    """
    def test_parse_nums(self):
        test_string = '00.5555 0.1121251-0.554666'
        ret = ' '.join(parse_nums(test_string))
        self.assertEqual(ret, '0.5555  0.11212 -0.55466')

    def test_trim_symbol(self):
        test_str = '[LMFAO - Party Rock Anthem ft. Lauren Bennett, GoonRock](https://www.youtube.com/watch?v=KQ6zr6kCPj8)'
        ret = trim_symbol(test_str)
        answer_str = 'LMFAO Party Rock Anthem ft. Lauren Bennett, GoonRock https://www.youtube.com/watch?v=KQ6zr6kCPj8 '
        self.assertEqual(ret, answer_str)

if __name__ == '__main__':
    unittest.main()