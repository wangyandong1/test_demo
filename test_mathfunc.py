# -*- coding: utf-8 -*-
import unittest
import mathfunc
class MathFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,mathfunc.test_add(1, 2))
        self.assertNotEqual(3,mathfunc.test_add(2, 2))
    def test_minus(self):
        self.assertEqual(1,mathfunc.test_minus(3, 2))
    def test_multi(self):
        self.assertEqual(6, mathfunc.test_multi(2, 3))
    def test_divide(self):
        self.assertEqual(2, mathfunc.test_divide(6, 3))
        self.assertEqual(2.5, mathfunc.test_divide(5, 2))
if __name__ == '__main__':
    unittest.main()

